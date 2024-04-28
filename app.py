import requests
import base64
import cv2
import os
import datetime
import time
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import subprocess

load_dotenv()


def detect_motion(threshold_area=5000):
    # get camera 
    cam = cv2.VideoCapture(0)
    
    gray_prev = None
    motion = False
    sending_request = False  # Flag to indicate if send_request is running

    while True:
        # Read a frame from the camera
        ret, frame = cam.read()
        
        # Convert to grayscale and apply Gaussian blur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        
        # Calculate the absolute difference between the current frame and the previous frame
        if gray_prev is not None and not sending_request:
            diff = cv2.absdiff(gray, gray_prev)
            
            # Threshold the difference image
            thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
            
            # Find contours in the thresholded image
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Iterate through the contours and calculate their area
            for contour in contours:
                area = cv2.contourArea(contour)
                
                # If the area exceeds the specified threshold
                if area > threshold_area:
                    print("Motion detected!")
                    motion = True
                    break
        
        # Update the previous frame
        gray_prev = gray
        if motion:
            cam.release()
            break

def take_image():
    # get camera 
    cam = cv2.VideoCapture(0)
    res, image = cam.read()

    if res:
        if not os.path.exists('images'):
            os.makedirs('images')
        
        # Get current date and time
        now = datetime.datetime.now()
        
        # Format the date and time as a string
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        
        # Create the file name with the timestamp
        filename = f"images/{timestamp}.png"
        
        # Save the image with the timestamped file name
        cv2.imwrite(filename, image)
        
        # release the cam
        cam.release()
        
        print(f"Image Taken {timestamp}")
        # Return the path of the saved image

        return filename
    else:
        print("Could not take image")
        cam.release()
        return None

def send_request(image_path):
    start_time = time.time()
    
    start_ollama()
    
    prompt = """
        This is a picture of my front door.  I need you to tell
        me what is going on at my front door. I already know what time
	of day it is and what is going on in the background. Just tell me 
	what the person at my front door is doing. I need to know quickly. 
        It needs to be short, super short, less than 50 words,
        short enough to be a brief text message.
    """
    url = "http://localhost:11434/api/generate"
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    print("----- Encoded Image -----")
    response = requests.post(url, json={
        "model": "llava",
        "prompt": prompt,
        "stream": False,
        "images": [encoded_image]

    })
    
    close_ollama_terminal()
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Function took {execution_time:.2f} seconds to run")
    return response.json()["response"]

def start_ollama():
    # Start ollama run llava in a new terminal window
    subprocess.Popen("ollama run llava", shell=True)
    print("---------- RUNNING OLLAMA ----------")
    
def close_ollama_terminal():
    # Check if the process is running
    if subprocess.call(["pgrep", "-f", "ollama run llava"]) == 0:
        # If the process is running, close it
        subprocess.Popen(["pkill", "-f", "ollama run llava"])
        print("---------- STOPPED OLLAMA ----------")
    else:
        print("No process found with command 'ollama run llava'")

def send_email_with_image(message, image_path):
    # Retrieve email addresses and credentials from .env file
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    
    mailtrap_username = os.getenv("MAILTRAP_USERNAME")
    mailtrap_password = os.getenv("MAILTRAP_PASSWORD")

    # Create an EmailMessage object
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Porch Bot'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Open the image file and attach it to the email
    with open(image_path, 'rb') as image:
        msg.add_attachment(image.read(), maintype='image', subtype='jpg', filename='image.jpg')

    # Send the email using SMTP
    with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
        server.starttls()
        server.login(mailtrap_username, mailtrap_password)
        server.sendmail(sender_email,receiver_email, msg.as_string())

def main():
    while True:
        print("Starting Loop")
        detect_motion()
        path = take_image()
        response = send_request(path)
        send_email_with_image(response, path)

if __name__ == "__main__":
    main()

# Porch Bot

<p align='center'>
  Tools Used
</p>

<p align='center'>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white" />
    <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" />
    <img src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white" />
    <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
</p>


Porch Bot is an AI powered surveillance program. It detects motion, snaps a pciture and uses [LLaVA](https://ollama.com/library/llava) 
running locally to describe what is going on in the image. The response and the image are then emailed to you so you can
know what is going on on your porch. 

You can follow the steps below to get started. You will need a USB camera, and some sort of computer. I'm running this on a 
Raspberry Pi 5 8GB and it takes around 4 minutes, so I'd recommend something stronger if you wanted quick responses.

### Mailtrap Account
First you will need to go create a free account with Mailtrap - this will allow you to email yourself the response - make sure to 
note your Mailtrap username and password found by clicking the **Sending Domains** tab on the left, then clikcing the **demomailtrap.com**
domain, and finally clikcing into the **SMTP/API Settings**. 

### Clone Repo and Set Up Env
Clone this repo and open a terminal. Then create a virtual environment using 
```
python -m venv venv
```
Next, you need to activate the virtual environment using one of the following: <br><br>
**MacOS/Linux**
```
source venv/bin/activate 
```
**Windows**
```
venv\Scripts\activate
```

You will see a `(venv)` at the front of your command line when your wirtual environment is actiavted. Now you 
need to install the dependencies. This can be done using
```
pip install -r requirements.txt
```

Now create a `.env` file to store some credentials
```
SENDER_EMAIL='mailtrap@demomailtrap.com'
MAILTRAP_EMAIL=[email used to sign up for mailtrap - where you message will be sent] 
MAILTRAP_USERNAME=[mailtrap username from earlier]
MAILTRAP_PASSWORD=[mailtrap password from earlier]
```

### Downloading Ollama and LLaVA Model
To run the LLaVA model locally, [ollama](https://ollama.com/) was used. You need to follow the instructions found [here](https://ollama.com/download)
to download ollama for your device. Then run the following to download the LLaVA model - it takes up arpund 5GB. 
```
ollama pull llava
```

### Running the Application
Now all thats left is to run the script:
```
python app.py
```
This will run until you manually stop it. 

You can contact me at berniejr01@gmail.com with any questions. As of 4/28/2024, 
I am on the hunt for entry level software engineer positions and would greatly appreciate if you share or star this repo in hopes of getting 
more eyes on my work. 


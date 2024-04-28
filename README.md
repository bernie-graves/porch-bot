# Porch Bot

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
Clone this repo then create a virtual environment using 
```
python -m venv venv
```

### Downloading Ollama and LLaVA Model

* Download the Ollama library using the following command: `git clone (link unavailable)
* Download the LLaVA model using the following command: `wget https://.../llava-model.pt`

### Setting up Virtual Environment and Installing Requirements

* Create a virtual environment using the following command: `python -m venv venv`
* Activate the virtual environment using the following command: `source venv/bin/activate` (on Mac/Linux) or `venv\Scripts\activate` (on Windows)
* Install the required packages using the following command: `pip install -r requirements.txt`

### Running the Application

* Run the application using the following command: `python app.py`

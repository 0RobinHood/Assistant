import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import wolframalpha
import wikipedia
import pyjokes
import pyautogui
from bs4 import BeautifulSoup
import os
import webbrowser
from selenium import webdriver
import subprocess
import request2
from twilio.rest import Client
from ecapture import ecapture as ec
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("I am your Assistant. what can i do for you")
	speak("this is robinhood!")
	speak(assname)
 #wishMe()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def iam():
    speak("I am your assistant")

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()

def take_command():
    
    try:
        with sr.Microphone() as source:
            
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
           
            
            if 'robin' in command:
                command = command.replace('robin', '')
                
    except:
        pass
    return command
            


def run_robin():
    command = take_command()
    print(command)




    if 'play music' in command or "play song" in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'adate' in command:
        date = datetime.now().strfdate('%D:%M:%Y')
        talk('current date is ' + adate)  
    elif 'about'in command:
        person = command.replace('about' , '')
        info = wikipedia.summary(person)
        print(info)
        talk(info)
    elif 'go to ' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'who' in command:
        iam()
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        webbrowser.open("chrome.com")
    elif 'open youtube' in command:
        speak('opening youtube...')
        webbrowser.open("youtube.com")
    elif 'calculate' in command:
        app_id = "wolframalpha api id"
        Client = wolframalpha.Client(app_id)
        indx = command.lower().split().index("calculate")
        command = command.split()[indx + 1:]
        res = Client.command(' '.join(command))
        answer = next(res.result).text
        print("the answer is " + answer)
        speak("the answer is " + answer)
    elif "camera " in command or "take a photo" in command:
        ec.capture(0, "RObinhoods camera","img.jpg")
        
        im = pyautogui.screenshot()
        im.save("robin.jpg")
        save = "C:\\Users\SUGURU BHARATHI\Desktop\\My files\\photos"
        os.startfile(save)
    elif "Search" in command:
        command = command.replace("Search", " ")
        input = command
        speak("searching..." + command)
        webbrowser.open(r"https://www.google.co.in /" + input )
    elif "tab" in command:
        dr = webdriver.chrome()
        dr.quit()
    elif "locate" in command:
        command = command.replace("locate"," ")
        location = command
        speak("searching" + command)
        speak(location)
        webbrowser.open("https://www.google.com / maps / place /" + location + "")
    
    elif 'send a mail' in command:
        try:
            speak('what should i say?')
            content = take_command()
            speak('for whom should i send !')
            to = input()
            sendEmail(to, content)
            speak('email has been sent !')
        except Exception as e:
            print(e)
            speak('i am not able to send mail !')
    elif 'how are you ' in command:
        speak("i am fine, and what about you!")
    elif 'fine' in command:
        speak('Its good to know that your fine')
       
    else:
        talk('Please say the command again.')
    
    

while True:
    run_robin()
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import randfacts
import time
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except UnboundLocalError:
        pass
    return command


def run_alexa():
    try:
        command = take_command()
        print(command)
        try:
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'say some interesting facts' in command:
                fat = randfacts.get_fact(filter_enabled=True)
                print(fat)
                talk(fat)
            elif 'jarvis' in command:
                talk('at your services sir')
            elif 'hai' in command:
                talk('hello')
            elif 'change the voice' in command:
                talk('sorry please change your settings')
            elif 'what is your name' in command:
                talk('jarvis iam Sebastian Thomas AI Assistant')
            elif 'open google' in command:
                webbrowser.open('https://www.google.com/')
            elif 'youtube' in command:
                talk('opening youtube')
                webbrowser.open('https://www.youtube.com/')
            elif 'whatsapp' in command:
                talk('opening whatsapp')
                webbrowser.open('https://web.whatsapp.com/')
            elif 'facebook' in command:
                talk('opening facebook')
                webbrowser.open('https://www.facebook.com/')
            elif 'internet speed test' in command:
                webbrowser.open('https://www.speedtest.net/')
            elif 'time' in command:
                Time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + Time)
            elif 'notepad' in command:
                os.system("C:\\Windows\\notepad.exe")

            elif 'who is the' in command:
                person = command.replace('who is the', '')
                info = wikipedia.search(person, results=5)
                print(info)
                talk(info)
            elif 'can you help me' in command:
                talk('yes sir!!')
            elif 'who is your boss' in command:
                talk('you sir !!!')
            elif 'how can you help me ' in command:
                talk('i can assistant you sir')
            elif 'date' in command:
                day = datetime.date.today()
                talk(day)
            elif 'good morning' in command:
                talk('good morning sir')
            elif 'good afternoon' in command:
                talk('good afternoon sir')
            elif 'are you single' in command:
                talk("Yes Iam single please don't ask me again")
            elif 'joke' in command:
                print(pyjokes.get_joke(language='en', category='neutral'))
                talk(pyjokes.get_joke())
            elif 'shutdown the pc' in command:
                talk("ok sir")
                pywhatkit.shutdown(10)
            elif 'who made you' in command:
                talk('one of the intelligent person')
            else:
                talk('Please say the command again.')
        except:
            pass
    except:
        pass


while True:
    time.sleep(1)
    run_alexa()

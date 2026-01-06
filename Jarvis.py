import datetime
import pyjokes as pyjokes
import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
from time import sleep
from bs4 import BeautifulSoup
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


from wishme import wishme
wishme()


def command():
    # Takes microphone's input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 10)

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again plz?")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = command().lower()
        # logic to execute task
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        elif "open google" in query:
            speak("Opening Google!")
            webbrowser.open("google.com")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        elif "open amazon" in query:
            webbrowser.open("amazon.in")
            speak("Opening Amazon")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        elif "open stackoverflow" in query:
            speak("Opening StackOverflow")
            webbrowser.open("stackoverflow.com")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        elif "open spotify" in query:
            speak("Opening Spotify!")
            webbrowser.open("spotify.com")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"The time is {time}")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

        elif "play music" in query:
            speak("Playing Music in 3")
            sleep(1)
            musicPath = "C:/Users/soham/OneDrive/Desktop/Som/Music/Kubbi-Ember.mp3"
            os.startfile(musicPath)
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

        elif "valorant" in query:
            path = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(path)
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

        elif "news" in query:
            from NewsRead import latestnews
            latestnews()
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

        elif "your creators" in query:
            print("I was created by Avishkar,Shrikant and Soham and their mentor was Karan Sir")
            speak("I was created by Avishkar,Shrikant and Sohum and their mentor was Karan Sir")
            sleep(1)

        elif "hello" in query:
            speak("Hello! I hope you are having a wonderful day!")
            sleep(1)

        elif "how are you" in query:
            speak("I am doing great, thanks for asking!")
            sleep(1)

        elif "how was your day" in query:
            speak("Its going great Sir, thanks for asking!")
            sleep(1)

        elif "great job" in query or "well done" in query:
            speak("Thank You Sir!")
            sleep(1)

        elif "Thanks" in query or "thank you" in query:
            speak("Your Welcome Sir!")
            sleep(1)

        elif "whatsapp message" in query:
            from whatsapp import sendMessage
            sendMessage()
            speak("Sending the message!")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

        elif "sleep" in query or "end program" in query:
            speak("Ok sir, going to sleep!")
            break

        elif "weather" in query or "temperature" in query:
            search = "temperature in pune"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

        elif "photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.sleep(2)
            pyautogui.press("enter")
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

        elif "tell me a joke" in query or "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            a = input("[Enter 1 to Continue] Or [Enter 2 to Stop]: ")
            if str(a) == "1":
                sleep(1)
                pass
            elif str(a) == "2":
                break

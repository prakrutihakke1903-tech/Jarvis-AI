import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=529cbfc7b3c34b7fae133f05f7f50da1",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=529cbfc7b3c34b7fae133f05f7f50da1",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=529cbfc7b3c34b7fae133f05f7f50da1",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=529cbfc7b3c34b7fae133f05f7f50da1",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=529cbfc7b3c34b7fae133f05f7f50da1",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=529cbfc7b3c34b7fae133f05f7f50da1"
        }

    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        break

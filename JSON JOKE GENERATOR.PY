import requests
import pyttsx3
import time

engine =  pyttsx3.init()
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

#Extract the joke

    setup = data["setup"]
    punchline = data["punchline"]

#Show joke

    print("Random Joke")
    print("Joke:",setup)
    print("Explaination:",punchline)

#Speak Joke

    engine.say(setup)
    engine.runAndWait()
    time.sleep(2)
    engine.say(punchline)
    engine.runAndWait()

else:
   print("Error")







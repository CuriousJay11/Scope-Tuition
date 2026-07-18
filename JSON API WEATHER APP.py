import requests
import pyttsx3

engine = pyttsx3.init()
response =requests.get("https://wttr.in/Bangalore?format=j1")
if response.status_code == 200:
    data = response.json()
    Temp = data["current_condition"][0]["temp_C"]
    Humidity = data["current_condition"][0]["humidity"]
    print("Temp:",Temp,"°C")
    print("Humidity:",Humidity)

else:
    print("error")





import requests

city = input("Enter City Of Choice: ")
url = "https://wttr.in/{city}?format=j1"
response =requests.get(url)
if response.status_code == 200:
    data = response.json()
    Temp = data["current_condition"][0]
    Humidity = data["current_condition"][0]
    Windspeed = data["current_condition"][0]
    print("Temp:",Temp["temp_C"],"°C")
    print("Humidity:",Humidity["humidity"])
    print("Windspeed:",Windspeed["windspeedKmph"],"km/h")
    
    engine.say(setup)
    engine.say(punchline)
    engine.runAndWait()

else:
    print("error")
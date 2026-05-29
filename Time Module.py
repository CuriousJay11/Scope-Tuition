import time

def timer(seconds):
    while seconds>0:
      print("Time left:",seconds)
      time.sleep(1)
      seconds = seconds-1
    print("Times up")

seconds = int(input("Enter time in seconds:"))
timer(seconds)
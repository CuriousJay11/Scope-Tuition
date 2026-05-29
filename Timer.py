import time

def countdown(seconds):
    while seconds:
        mins = seconds//60
        secs = seconds%60
        print(f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        seconds-=1
    print("Timer Done")

timersec = int(input("Enter seconds:"))
countdown(timersec)


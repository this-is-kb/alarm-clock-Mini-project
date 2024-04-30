from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def countdown(time_seconds):
    time_left = time_seconds

    print(CLEAR)
    while 0 < time_left <= time_seconds:
        time.sleep(1)
        time_left = time_left - 1

        minutes = time_left // 60
        seconds = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes:02d}:{seconds:02d}")

    print(f"{CLEAR_AND_RETURN}The alarm should ring now")
    playsound("Funny_alarm.mp3")

print("After how much time do you want to ring the alarm? ")
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
total_time = minutes*60 + seconds
countdown(total_time)
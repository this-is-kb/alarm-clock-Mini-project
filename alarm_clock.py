import time

def countdown(time_seconds):
    time_left = time_seconds

    while 0 < time_left <= time_seconds:
        time.sleep(1)
        time_left = time_left - 1

        minutes = time_left // 60
        seconds = time_left % 60

        print(f"{minutes}:{seconds}")

    print("The alarm should ring now")

countdown(10)
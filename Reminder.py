from pygame import mixer
from datetime import datetime
from time import time
from plyer import notification

def musiconloop(stopper): #making a function which plays the Alarm sound and breaks when type Done
    mixer.init()
    mixer.music.load("/home/sachin/Downloads/alarm")
    while True:
        mixer.music.play()
        input_of_user = input()
        if input_of_user == 'Done':
            mixer.music.stop()
            break
        else:
            print("Not Valid. You need to type 'Done'")

def Store(data):
    with open("Data-->Water & Knees.txt", "a") as f:
        f.write(f"{data} {datetime.now()}\n")

if __name__ == '__main__':
    water_time = time()
    eye_time = time()
    water_alarmtime = 90*60
    eye_alarmtime = 45*60

    while True:
        if time() - water_time > water_alarmtime:
            notification.notify(title="Drink Water ", message="Type 'Done' in console to quit", timeout=15)
            musiconloop('Done')
            water_time = time()
            Store("Drank Water at")

        if time() - eye_time > eye_alarmtime:
            notification.notify(title = "Rest your Eyes Look Around" , message = "Don't look" , timeout = 15)
            musiconloop('Done')
            eye_time = time()
            Store("Rested my Eyes")



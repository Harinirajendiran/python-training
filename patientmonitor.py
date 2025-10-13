import threading
import time
import random

#-----func 1: Reading patient sensor data---

def read_sensor_data():
    for i in range(5):
        heart_rate=random.randint(60,120)
        temperature=round(random.uniform(36.5,39.0),1)
        print(f"Reading {i+1}: Heart Rate={heart_rate} bpm, Temperature={temperature} °C")
        time.sleep(2)

#-----func 2: sending doctor notificaton---
def notify_doctor():
    for i in range(5):
        print(f"Notification {i+1}: Patient vitals are stable.")
        time.sleep(9)
#---func 3: logging data----
def log_data():
    for i in range(5):
        print(f"Log {i+1}: Data logged successfully.")
        time.sleep(10)
        
#----creating threads---
t1=threading.Thread(target=read_sensor_data)
t2=threading.Thread(target=notify_doctor)
t3=threading.Thread(target=log_data)

#---starting thread---
t1.start()
t2.start()
t3.start()

#---waiting for threads to complete---
t1.join()
t2.join()
t3.join()

print("All tasks completed.")
from Backend import Read_Voltage, Voltage_to_Weight
import time
import csv

import RPi.GPIO as GPIO  # import GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)

GPIO.output(32,1)


t1 = time.time()
print("hit")
w = Read_Voltage(20)
print("hit")
t2 = time.time()
t = (t1 + t2)/2

t=5
w=100

with open('weights.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([t,w])

GPIO.cleanup()
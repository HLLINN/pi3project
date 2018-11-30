import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

led = GPIO.PWM(18, 100)
ledblue = GPIO.PWM(23, 100)
led.start(100)
ledblue.start(100)

while True:
	for i in range(0, 101):
		 led.ChangeDutyCycle(i)
		 ledblue.ChangeDutyCycle(100-i) #ledblue and led breath alternatively
		 time.sleep(.02)
	for n in range(0, 101):
		 led.ChangeDutyCycle(100-n)
		 ledblue.ChangeDutyCycle(n) #ledblue and led breath alternatively
		 time.sleep(.02)
		 
GPIO.cleanup()

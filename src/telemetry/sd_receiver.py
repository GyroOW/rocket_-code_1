import RPi.GPIO as GPIO
import time

RF_PIN: int = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(RF_PIN, GPIO.IN)

def receive_data() -> None:
    if GPIO.input(RF_PIN):
        print("Data Received")

while True:
    receive_data()
    time.sleep(1)

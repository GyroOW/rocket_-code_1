import RPi.GPIO as GPIO
import time

RF_PIN: int = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RF_PIN, GPIO.OUT)

def send_data(data: str) -> None:
    GPIO.output(RF_PIN, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(RF_PIN, GPIO.LOW)
    print(f"Data Sent: {data}")

while True:
    send_data("Telemetry Data")
    time.sleep(1)

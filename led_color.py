import time
from machine import Pin
time.sleep(0.1) # Wait for USB to become ready

leds = {
    "red":Pin(16,Pin.OUT),
    "green":Pin(18,Pin.OUT),
    "blue":Pin(20,Pin.OUT)
}
while True:
    color = input("Please provide color (red, blue and green)").lower()
    if color in leds:
        for led in leds.values():
            led.value(1)
        leds[color].value(0)
    else:
        print("Invalid Input")
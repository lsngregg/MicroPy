# Building up things to inport
# Going to keep the blinking light just to know "main" is running

from machine import Pin, Timer, I2C
import adafruit_tsl2591

#Blink the LED
led = Pin(25, Pin.OUT)
LED_state = True
tim = Timer()

def tick(timer):
    global led, LED_state
    LED_state = not LED_state
    led.value(LED_state)
    
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)

def getLux():
    # Insert code for TSL here
    pass

def Lux2EV(lux):
    #gonna convert lux to EV
    pass


#Initialize I2C bus
sda = machine.Pin(16)
scl = machine.Pin(17)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

#Get/scan for i2c devices
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c devices found.")
    
else:
    print("i2c devices found: ", len(devices))
    
for device in devices:
    print("Decimal address: ", device, " Hex address: ", hex(device))

sensor = adafruit_tsl2591.TSL2591(i2c)

lux = sensor.lux
print("Total light: {0}lux".format(lux))


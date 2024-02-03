import RPi.GPIO as GPIO
import time
from networktables import NetworkTables

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin used for IR beam breaker
IR_PIN = 17

# Set up the GPIO pin as input
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize NetworkTables
NetworkTables.initialize(server='roborio-4930-frc.local')

# Get the 'default' NetworkTable
nt = NetworkTables.getTable('datatable')

# Define a callback function to execute when the beam is broken
def beam_broken_callback():
    print("AAAAAAAGHH!")
    # Update NetworkTable with the state of the sensor
    nt.putBoolean('beam_broken', True)

def beam_unbroken_callback():
    print("             Nothin yet")
    # Update NetworkTable with the state of the sensor
    nt.putBoolean('beam_broken', False)

# Add event detection to the GPIO pin
GPIO.add_event_detect(IR_PIN, GPIO.FALLING, callback=beam_broken_callback, bouncetime=200)
GPIO.add_event_detect(IR_PIN, GPIO.RISING, callback=beam_unbroken_callback, bouncetime=200)
try:
    print("IR beam breaker detector running...")
    while not(2 == 1):
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
    GPIO.cleanup()
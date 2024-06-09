import RPi.GPIO as GPIO
import time
import util as ut

# Set the GPIO mode
ut.init_gpio()

# Define the GPIO pins for the ultrasonic sensors
TRIG1 = 2
ECHO1 = 3
TRIG2 = 19
ECHO2 = 26

# Set up the GPIO pins for the first sensor
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)

# Set up the GPIO pins for the second sensor
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

def measure_distance(trig, echo):
    # Send a 10us pulse to the TRIG pin
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    # Measure the duration of the ECHO pin's high signal
    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    # Calculate the distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound in cm/s divided by 2
    return round(distance, 2)

try:
    while True:
        dist1 = measure_distance(TRIG1, ECHO1)
        dist2 = measure_distance(TRIG2, ECHO2)
        
        print(f"dist1: {dist1} cm, dist2: {dist2} cm")
        
        # Threshold distance in cm to consider an obstacle
        threshold_distance = 30

        if dist1 < threshold_distance and dist2 < threshold_distance:
            ut.stop()
            print("Obstacle detected! Stopping the robot.")
        elif dist1 > dist2:
            ut.right()
            print("Turning right...")
            time.sleep(0.5)  # Add delay to prevent rapid switching
            ut.stop()
        elif dist1 < dist2:
            ut.left()
            print("Turning left...")
            time.sleep(0.5)  # Add delay to prevent rapid switching
            ut.stop()

        time.sleep(0.1)  # Small delay to avoid rapid loop execution

except KeyboardInterrupt:
    GPIO.cleanup()

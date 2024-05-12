import RPi.GPIO as GPIO
import time
from config import ENABLE_PIN1, INPUT1_PIN1, INPUT2_PIN1, ENABLE_PIN2, INPUT1_PIN2, INPUT2_PIN2, PWM_FREQ

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENABLE_PIN1, GPIO.OUT)
    GPIO.setup(INPUT1_PIN1, GPIO.OUT)
    GPIO.setup(INPUT2_PIN1, GPIO.OUT)
    GPIO.setup(ENABLE_PIN2, GPIO.OUT)
    GPIO.setup(INPUT1_PIN2, GPIO.OUT)
    GPIO.setup(INPUT2_PIN2, GPIO.OUT)

    global pwm1, pwm2
    pwm1 = GPIO.PWM(ENABLE_PIN1, PWM_FREQ)
    pwm2 = GPIO.PWM(ENABLE_PIN2, PWM_FREQ)
    pwm1.start(0)
    pwm2.start(0)

def cleanup():
    GPIO.cleanup()

def set_motor_speed1(speed1):
    pwm1.ChangeDutyCycle(speed1)
   
def set_motor_speed2(speed2):
    pwm2.ChangeDutyCycle(speed2)

def forward(tf):
    GPIO.output(INPUT1_PIN1, True)
    GPIO.output(INPUT2_PIN1, False)
    GPIO.output(INPUT1_PIN2, True)
    GPIO.output(INPUT2_PIN2, False)
    time.sleep(tf)

def reverse(tf):
    GPIO.output(INPUT1_PIN1, False)
    GPIO.output(INPUT2_PIN1, True)
    GPIO.output(INPUT1_PIN2, False)
    GPIO.output(INPUT2_PIN2, True)
    time.sleep(tf)

def left(tf):
    GPIO.output(INPUT1_PIN1, True)
    GPIO.output(INPUT2_PIN1, False)
    GPIO.output(INPUT1_PIN2, False)
    GPIO.output(INPUT2_PIN2, True) # False
    time.sleep(tf)

def right(tf):
    GPIO.output(INPUT1_PIN1, False)
    GPIO.output(INPUT2_PIN1, True) # False
    GPIO.output(INPUT1_PIN2, True)
    GPIO.output(INPUT2_PIN2, False)
    time.sleep(tf)

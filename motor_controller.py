import RPi.GPIO as GPIO
import time
from config import ENABLE_PIN1, INPUT1_PIN1, INPUT2_PIN1, ENABLE_PIN2, INPUT1_PIN2, INPUT2_PIN2, PWM_FREQ

# Default speeds, adjust these values as needed for your application
DEFAULT_SPEED1 = 50
DEFAULT_SPEED2 = 50

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

def forward(tf, **kwargs):
    speed1 = kwargs.get('speed1', DEFAULT_SPEED1)
    speed2 = kwargs.get('speed2', DEFAULT_SPEED2)
    set_motor_speed1(speed1)
    set_motor_speed2(speed2)
    GPIO.output(INPUT1_PIN1, True)
    GPIO.output(INPUT2_PIN1, False)
    GPIO.output(INPUT1_PIN2, True)
    GPIO.output(INPUT2_PIN2, False)
    time.sleep(tf)
    set_motor_speed1(0)
    set_motor_speed2(0)

def reverse(tf, **kwargs):
    speed1 = kwargs.get('speed1', DEFAULT_SPEED1)
    speed2 = kwargs.get('speed2', DEFAULT_SPEED2)
    set_motor_speed1(speed1)
    set_motor_speed2(speed2)
    GPIO.output(INPUT1_PIN1, False)
    GPIO.output(INPUT2_PIN1, True)
    GPIO.output(INPUT1_PIN2, False)
    GPIO.output(INPUT2_PIN2, True)
    time.sleep(tf)
    set_motor_speed1(0)
    set_motor_speed2(0)

def left(tf, **kwargs):
    speed1 = kwargs.get('speed1', DEFAULT_SPEED1)
    speed2 = kwargs.get('speed2', DEFAULT_SPEED2)
    set_motor_speed1(speed1)
    set_motor_speed2(speed2)
    GPIO.output(INPUT1_PIN1, True)
    GPIO.output(INPUT2_PIN1, False)
    GPIO.output(INPUT1_PIN2, False)
    GPIO.output(INPUT2_PIN2, True)
    time.sleep(tf)
    set_motor_speed1(0)
    set_motor_speed2(0)

def right(tf, **kwargs):
    speed1 = kwargs.get('speed1', DEFAULT_SPEED1)
    speed2 = kwargs.get('speed2', DEFAULT_SPEED2)
    set_motor_speed1(speed1)
    set_motor_speed2(speed2)
    GPIO.output(INPUT1_PIN1, False)
    GPIO.output(INPUT2_PIN1, True)
    GPIO.output(INPUT1_PIN2, True)
    GPIO.output(INPUT2_PIN2, False)
    time.sleep(tf)
    set_motor_speed1(0)
    set_motor_speed2(0)

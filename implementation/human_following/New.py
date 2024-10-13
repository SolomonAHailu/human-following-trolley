






import RPi.GPIO as GPIO
import util as ut
import time
GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme

ut.init_gpio()

GPIO.setup(20, GPIO.OUT)# set GPIO 20 as output pin
GPIO.setup(21, GPIO.OUT)# set GPIO 21 as output pin
      
pin20 = GPIO.PWM(20, 100)    # create object pin20 for PWM on port 20 at 100 Hertz
pin21 = GPIO.PWM(21, 100)    # create object pin21 for PWM on port 21 at 100 Hertz

val=100 # maximum speed
pin20.start(val)              # start pin20 on 0 percent duty cycle (off)  
pin21.start(val)              # start pin21 on 0 percent duty cycle (off)  


print("speed set to: ", val)
#------------------------------------------
ut.forward()
time.sleep(2)
ut.cleanup_gpio()

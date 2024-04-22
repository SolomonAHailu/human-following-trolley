from gpiozero import Motor
import config 
from time import sleep

class MotorController:
	def __init__(self):
		self.left_motor = Motor(config.LEFT_MOTOR_FORWARD_PIN, config.LEFT_MOTOR_BACKWARD_PIN)
		self.right_motor = Motor(config.RIGHT_MOTOR_FORWARD_PIN, config.RIGHT_MOTOR_BACKWARD_PIN)
		
	def move_forward(self, duration):
		self.left_motor.forward()
		self.right_motor.forward()
		sleep(duration)
		self.left_motor.stop()
		self.right_motor.stop()

		
	def move_backward(self, duration):
		self.left_motor.backward()
		self.right_motor.backward()
		sleep(duration)
		self.left_motor.stop()
		self.right_motor.stop()

		
	def turn_left(self, duration):
		self.left_motor.backward()
		self.right_motor.forward()
		sleep(duration)
		self.left_motor.stop()
		self.right_motor.stop()

		
	def turn_right(self, duration):
		self.left_motor.forward()
		self.right_motor.backward()
		sleep(duration)
		self.left_motor.stop()
		self.right_motor.stop()


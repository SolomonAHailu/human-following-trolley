from hardware import MotorController
from time import sleep 
import bluetooth

def setup_bluetooth_server():
	server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	port = 1
	server_socket.bind(("", port))
	server_socket.listen(1)
	print("waiting to connect...")
	cleint_socket, client_info = server_socket.accept()
	print("Connected...")
	return cleint_socket, server_socket

def main():
	robot = MotorController()
	client_socket, server_socket = setup_bluetooth_server()
	
	print("connection stablished")
	
	#test movements
	robot.move_forward(2)
	sleep(1)
	robot.move_backward(2)
	sleep(1)
	robot.turn_left(1)
	sleep(1)
	robot.turn_right(1)


if __name__ == "__main__":
	main()

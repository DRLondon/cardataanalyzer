import obd
import socket


class SocketGetter(object):
	def __init__(self):
		self.host = socket.gethostname()
		self.port = 8080
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.host, self.port))

	@classmethod
	def do_stuff(self):
		self.sock.sendall(b'Hello World')
		self.data = self.sock.recv(1024)
		
	@classmethod
	def finalize(self):
		self.sock.close()
		print('Received', repr(self.data))



class CarDataAnalyzer(object):
	def __init__(self):
		self.connection = obd.OBD()
		self.speed_command = obd.commands.SPEED
		self.rpm_command = obd.commands.RPM
		self.fuel_command = obd.commands.FUEL_LEVEL

	@classmethod
	def get_speed(self):
		return self.connection.query(self.speed_command)
	
	@classmethod
	def get_rpm(self):
		return self.connection.query(self.rpm_command)
	
	@classmethod
	def get_fuel_level(self):
		return self.connection.query(self.fuel_command)

	
car_data = CarDataAnalyzer()
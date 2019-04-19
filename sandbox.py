import obd

class CarDataAnalyzer(object):
    def __init__(self):
        self.connection = obd.OBD()
        self.speed_command = obd.commands.SPEED
        self.rpm_command = obd.commands.RPM
        self.fuel_command = obd.commands.FUEL_LEVEL

    def get_speed(self):
        return self.connection.query(self.speed_command)

    def get_rpm(self):
        return self.connection.query(self.rpm_command)

    def get_fuel_level(self):
        return self.connection.query(self.fuel_command)

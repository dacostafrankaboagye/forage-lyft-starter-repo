from .tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_sensor_values):
        self.tire_wear_sensor_values = tire_wear_sensor_values

    def needs_service(self):
        sum_of_values = sum(self.tire_wear_sensor_values)
        if sum_of_values >= 3.0:
            return True
        return False


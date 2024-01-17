from .tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_sensor_values):
        self.tire_wear_sensor_values = tire_wear_sensor_values

    def needs_service(self):
        for value in self.tire_wear_sensor_values:
            if value >= 0.9:
                return True 
        return False

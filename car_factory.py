from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

from car import Car

from datetime import datetime

class CarFactory:
    
    #   capulet engine with  spindler battery
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor_values):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_sensor_values)
        return Car(engine, battery, tire)
    
    #   willoughby engine with spindler battery
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor_values):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear_sensor_values)
        return Car(engine, battery, tire)
    
    #   sternman engine with spindler battery
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_sensor_values):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_sensor_values)
        return Car(engine, battery, tire)
    
    #   willoughby engine with Nubbin battery
    @staticmethod
    def  create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor_values):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear_sensor_values)
        return Car(engine, battery, tire)

    #   capulet engine with nubbin battery
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor_values):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_sensor_values)
        return Car(engine, battery, tire)


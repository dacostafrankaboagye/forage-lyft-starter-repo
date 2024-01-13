'''from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
'''
from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery

class Car(Serviceable):

    def __init__(self, engine, battery):
        self.engine = Engine()
        self.battery = Battery()

    def needs_service(self):
        engine_needs_service = self.engine.needs_service()
        battery_needs_service = self.battery.needs_service()
        return engine_needs_service or battery_needs_service


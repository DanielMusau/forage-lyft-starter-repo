# from abc import ABC, abstractmethod


# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass

from engine.engine import Engine
from battery.battery import Battery

class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    fuel = 0
    fuel_consumption = 0
    weight = 0

    def __init__(self, weight:int, fuel:int, fuel_consumption:int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False and self.fuel > 0:
            self.started = True
        elif self.started == False and self.fuel == 0:
            raise LowFuelError

    def move(self, dictance:int):
        remaining_fuel = self.fuel - self.fuel_consumption * dictance
        if remaining_fuel >= 0:
            self.fuel = remaining_fuel
        else:
            raise NotEnoughFuel
        

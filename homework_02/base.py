from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    started = False

    def start(self):
        if self.started == False and self.fuel > 0:
            self.started = True
        elif self.started == False and self.fuel == 0:
            raise LowFuelError

    def move(self, dictance):
        remaining_fuel = self.fuel - self.fuel_consumption * dictance
        if remaining_fuel >= 0:
            self.fuel = remaining_fuel
        else:
            raise NotEnoughFuel
        

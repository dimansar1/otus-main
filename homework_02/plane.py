"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = 0
    
    def __init__(self, weight:int, fuel:int, fuel_consumption:int, max_cargo:int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
    

    def load_cargo(self, plus_cargo:int):
        new_cargo = self.cargo + plus_cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload
    
    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo

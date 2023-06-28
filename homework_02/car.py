"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle

class Car(Vehicle):
    engine = None
    def set_engine(self, object):
        self.engine = object
        
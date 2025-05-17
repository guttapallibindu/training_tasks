from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Bike(Vehicle):
    def fuel_type(self):
        print("Bike uses petrol")
    def ownmethod(self):
        print("Biek uses petrol")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("electric car uses battery")

v = Vehicle()
b = Bike()

b.fuel_type()
#e.fuel_type()

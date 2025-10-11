from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def speed(self):
        pass


# BMW class
class BMW(Vehicle):
    def start(self):
        return "BMW starts with a smooth roar!"

    def speed(self):
        return "BMW top speed: 250 km/h"
class Ferrari(Vehicle):
    def start(self):
        return "Ferrari starts with a loud V8 sound!"
    def speed(self):
        return "Ferrari top speed: 340 km/h"
def show_vehicle_details(vehicle):
    print(vehicle.start())
    print(vehicle.speed())
    print("-" * 40)
if __name__ == "__main__":
    bmw = BMW()
    ferrari = Ferrari()
    for car in (bmw, ferrari):
        show_vehicle_details(car)
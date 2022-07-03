# from inheritance_exercises.need_for_speed.project.vehicle import Vehicle
from .vehicle import Vehicle


class Car(Vehicle):

    fuel_consumption = 3
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

# from inheritance_exercises.need_for_speed.project.vehicle import Vehicle
from .vehicle import Vehicle


class Motorcycle(Vehicle):

    DEFAULT_FUEL_CONSUMPTION = V

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

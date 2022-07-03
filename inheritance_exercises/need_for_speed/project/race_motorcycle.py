# from inheritance_exercises.need_for_speed.project.motorcycle import Motorcycle
from .motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):

    fuel_consumption = 8
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

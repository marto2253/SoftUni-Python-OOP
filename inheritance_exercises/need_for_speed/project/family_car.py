from inheritance_exercises.need_for_speed.project.car import Car
# from .car import Car


class FamilyCar(Car):

    fuel_consumption = Car.fuel_consumption
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)


family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

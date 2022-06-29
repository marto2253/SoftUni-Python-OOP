class Flower:

    is_happy = False

    def __init__(self, name: str, water_requirement: int):
        self.name = name
        self.water_requirement = water_requirement

    def water(self, quantity):
        if quantity >= self.water_requirement:
            Flower.is_happy = True

    def status(self):
        if Flower.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

# from inheritance_exercises.shop.project.product import Product
from .product import Product

class Drink(Product):
    def __init__(self, name, quantity=10):
        super().__init__(name, quantity)

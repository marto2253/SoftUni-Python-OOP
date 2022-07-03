# from inheritance_exercises.shop.project.product import Product
from .product import Product


class Food(Product):
    def __init__(self, name, quantity=15):
        super().__init__(name, quantity)
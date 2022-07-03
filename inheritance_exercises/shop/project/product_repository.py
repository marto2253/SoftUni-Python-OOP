# from inheritance_exercises.shop.project.food import Food
# from inheritance_exercises.shop.project.drink import Drink
# from inheritance_exercises.shop.project.product import Product
from .product import Product
from .food import Food
from .drink import Drink


class ProductRepository:

    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = ''

        for product in self.products:
            result += f'{product.name}: {product.quantity}\n'

        return result.strip()


# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)

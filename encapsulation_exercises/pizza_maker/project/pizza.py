# from encapsulation_exercises.pizza_maker.project.dough import Dough
# from encapsulation_exercises.pizza_maker.project.topping import Topping
from .dough import Dough
from .topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) == 0:
            raise ValueError("The name cannot be an empty string")
        self.__name = name
        
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, dough):
        if dough is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        if toppings_capacity <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        weight = 0
        weight += self.dough.weight
        for v in self.toppings.values():
            weight += v

        return weight


from .worker import Worker
# from encapsulation_exercises.wild_cat_zoo.project.worker import Worker


class Caretaker(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)


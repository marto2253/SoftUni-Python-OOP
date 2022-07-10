from .caretaker import Caretaker
from .cheetah import Cheetah
from .keeper import Keeper
from .lion import Lion
from .tiger import Tiger
from .vet import Vet
from .animal import Animal
from .worker import Worker

# from encapsulation_exercises.wild_cat_zoo.project.cheetah import Cheetah
# from encapsulation_exercises.wild_cat_zoo.project.caretaker import Caretaker
# from encapsulation_exercises.wild_cat_zoo.project.keeper import Keeper
# from encapsulation_exercises.wild_cat_zoo.project.lion import Lion
# from encapsulation_exercises.wild_cat_zoo.project.tiger import Tiger
# from encapsulation_exercises.wild_cat_zoo.project.vet import Vet
# from encapsulation_exercises.wild_cat_zoo.project.animal import Animal
# from encapsulation_exercises.wild_cat_zoo.project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"





    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = 0
        for worker in self.workers:
            sum_of_salaries += worker.salary

        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_animal_expenses = 0
        for animal in self.animals:
            sum_of_animal_expenses += animal.money_for_care

        if self.__budget >= sum_of_animal_expenses:
            self.__budget -= sum_of_animal_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ''

        result += f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [t for t in self.animals if isinstance(t, Tiger)]
        cheetahs = [c for c in self.animals if isinstance(c, Cheetah)]

        for lion in lions:
            result += f'----- {len(lions)} Lions:\n'
            result += f'{lion.__repr__()}\n'

        for tiger in tigers:
            result += f'----- {len(tigers)} Tigers:\n'
            result += f'{tiger.__repr__()}\n'

        for cheetah in cheetahs:
            result += f'----- {len(cheetahs)} Cheetahs:\n'
            result += f'{cheetah.__repr__()}\n'

        return result.strip()

    def workers_status(self):
        result = ''

        result += f'You have {len(self.workers)} workers\n'

        vets = [v for v in self.workers if isinstance(v, Vet)]
        keepers = [k for k in self.workers if isinstance(k, Keeper)]
        caretakers = [c for c in self.workers if isinstance(c, Caretaker)]

        for keeper in keepers:
            result += f'----- {len(keepers)} Keepers:\n'
            result += f'{keeper.__repr__()}\n'

        for caretaker in caretakers:
            result += f'----- {len(caretakers)} Caretakers:\n'
            result += f'{caretaker.__repr__()}\n'

        for vet in vets:
            result += f'----- {len(vets)} Vets:\n'
            result += f'{vet.__repr__()}\n'

        return result.strip()
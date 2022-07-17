# from class_and_static_methods_exercises.gym.project.customer import Customer
# from class_and_static_methods_exercises.gym.project.equipment import Equipment
# from class_and_static_methods_exercises.gym.project.exercise_plan import ExercisePlan
# from class_and_static_methods_exercises.gym.project.trainer import Trainer
# from class_and_static_methods_exercises.gym.project.subscription import Subscription

from .subscription import Subscription
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .trainer import Trainer
from .customer import Customer

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, plan.equipment_id)

        return subscription.__repr__() + '\n' + customer.__repr__() + '\n' + trainer.__repr__() + \
            '\n' + equipment.__repr__() + '\n' + plan.__repr__()

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity


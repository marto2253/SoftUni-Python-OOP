# from class_and_static_methods_exercises.movie_world.project.customer import Customer
# from class_and_static_methods_exercises.movie_world.project.dvd import DVD
from .dvd import DVD
from .customer import Customer


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_age_rest = 0
        is_rented = False
        dvd_name = ''
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                dvd_age_rest = dvd.age_restriction
                dvd_name = dvd.name
                if dvd.is_rented:
                    is_rented = True
        for customer in self.customers:
            if customer.id == customer_id:
                if customer.age < dvd_age_rest:
                    return f"{customer.name} should be at least {dvd_age_rest} to rent this movie"
                elif dvd_name in customer.rented_dvds:
                    return f"{customer.name} has already rented {dvd_name}"
                elif dvd_name not in customer.rented_dvds and is_rented:
                    return "DVD is already rented"
                else:
                    customer.rented_dvds.append(dvd_name)
                    for dvd in self.dvds:
                        if dvd.id == dvd_id:
                            dvd.is_rented = True
                    return f"{customer.name} has successfully rented {dvd_name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd_name = ''
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                dvd_name = dvd.name

        for customer in self.customers:
            if customer.id == customer_id:
                if dvd_name in customer.rented_dvds:
                    customer.rented_dvds.remove(dvd_name)
                    for dvd in self.dvds:
                        if dvd.id == dvd_id:
                            dvd.is_rented = False
                    return f"{customer.name} has successfully returned {dvd_name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''

        result += '\n'.join([c.__repr__() for c in self.customers])
        result += '\n'
        result += '\n'.join([d.__repr__() for d in self.dvds])

        return result.strip()


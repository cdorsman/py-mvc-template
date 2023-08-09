from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        pass

    @abstractmethod
    def create(self, item):
        """Creates an object"""
        pass

    @property
    @abstractmethod
    def item_type(self):
        pass


class ProductModel(Model):
    class Price(float):
        """A polymorphic way to pass a float with a particular
        __str__ functionality."""

        def __str__(self):
            return f"{self:.2f}"

    products = {
        "milk": {"price": Price(1.50), "quantity": 10},
        "eggs": {"price": Price(0.20), "quantity": 100},
        "cheese": {"price": Price(2.00), "quantity": 10},
    }

    item_type = "product"

    def __iter__(self):
        yield from self.products

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")

class PersonnelModel(Model):
    employees = {
        "nick": {"first name": "Nick", "last name": "Doe", "date of birth": "1986"},
        "mike": {"first name": "Mike", "last name": "Doe", "date of birth": "1985"},
        "joe": {"first name": "Joe", "last name": "Doe", "date of birth": "1984"},
    }

    item_type = "employee"

    def __iter__(self):
        yield from self.employees

    def get(self, employee):
        try:
            return self.employees[employee]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")

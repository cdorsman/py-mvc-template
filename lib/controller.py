from abc import ABC, abstractmethod
from typing import List

class Controller(ABC):
    @abstractmethod
    def show_items(self):
        pass

    @abstractmethod
    def show_item_information(self, item):
        pass

class ProductController(Controller):
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)


class PersonnelController(Controller):
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)

#from abc import ABC, abstractmethod
from typing import List

#class Controller(ABC):
#    def __init__(self, model, view):
#        self.model = model
#        self.view = view
#
#    @abstractmethod
#    def show_items(self):
#        ...
#
#    @abstractmethod
#    def show_item_information(self, item):
#        ...

#class ProductController(Controller):
class ProductController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        """
        Show information about a {item_type} item.
        :param str item_name: the name of the {item_type} item to show information about
        """
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)


#class PersonnelController(Controller):
class PersonnelController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        """
        Show information about a {item_type} item.
        :param str item_name: the name of the {item_type} item to show information about
        """
        try:
            item_info = self.model.get(item_name)
        except Exception:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)

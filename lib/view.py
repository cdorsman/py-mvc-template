from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def show_item_list(self, item_type, item_list):
        pass

    @abstractmethod
    def show_item_information(self, item_type, item_name, item_info):
        """Will look for item information by iterating over key,value pairs
        yielded by item_info.items()"""
        pass

    @abstractmethod
    def item_not_found(self, item_type, item_name):
        pass


class ConsoleView(View):
    def show_item_list(self, item_type, item_list):
        print(item_type.upper() + " LIST:")
        for item in item_list:
            print(item)
        print("")

    @staticmethod
    def capitalizer(string):
        return string[0].upper() + string[1:].lower()

#    def show_item_information(self, item_type, item_name, item_info):
#        print(item_type.upper() + " INFORMATION:")
#        printout = "Name: %s" % item_name
#        for key, value in item_info.items():
#            printout += ", " + self.capitalizer(str(key)) + ": " + str(value)
#        printout += "\n"
#        print(printout)

    def show_item_information(self, item_type, item_name, item_info):
        print(item_type.upper() + f" INFORMATION of username {item_name} \n")
        labels = ""
        printout = ""
        
        for key, value in item_info.items():        
            labels += (str(key)).upper() + "\t"
        
        print(labels)

        for key, value in item_info.items(): 
            printout += str(value) + "\t\t"

        print(printout)

    def item_not_found(self, item_type, item_name):
        print(f'That {item_type} "{item_name}" does not exist in the records')

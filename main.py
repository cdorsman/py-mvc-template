#!/usr/bin/env python3

from sys import argv

from lib.parser import Parser
from lib.router import Router
from lib.model import PersonnelModel, ProductModel
from lib.view import ConsoleView 
from lib.controller import ProductController, PersonnelController


#def application(args)):
#    
#    router = Router()
#    router.register_controller('personel', PersonnelController, PersonnelModel, ConsoleView)
#    router.register_controller('product', ProductController, ProductModel, ConsoleView)
      
    #for route in router.routes:
    #    print(route)
    #    for path in args:
    #        if path == route:
#    return router.resolve(args)

def main():
    router = Router()
    name = ""   
 
    #router.register_controller('personnel', PersonnelController, PersonnelModel, ConsoleView)
    router.register_controller('product', ProductController, ProductModel, ConsoleView)

    for arg in argv[1:]:
        name = arg

    controller = router.resolve(name)
    controller.show_items()

if __name__ == "__main__":
    main()

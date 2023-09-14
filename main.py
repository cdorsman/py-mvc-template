#!/usr/bin/env python3

from sys import argv, dont_write_bytecode

from lib.parser import Parser
from lib.router import Router
from lib.model import PersonnelModel, ProductModel
from lib.view import ConsoleView 
from lib.controller import ProductController, PersonnelController


def main():
    router = Router()
    name = ""   
 
    router.register("product", ProductController, ProductModel, ConsoleView)

    name = argv[1]

    controller = router.resolve(name)
    if hasattr(controller, "show_items"):
        controller.show_items()

if __name__ == "__main__":
    dont_write_bytecode = True
    main()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from sys import exit

coffeemaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == 'off':
        exit()
    elif order == 'report':
        coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)


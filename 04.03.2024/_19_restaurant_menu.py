"""Write program for building restaurant menu using class in Python."""
class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_menu_item(self, item, price):
        self.menu_items[item] = price

    def print_menu(self):
        for item, price in self.menu_items.items():
            print(f"{item}: {price}")

obj = Menu()

obj.add_menu_item("Tea", 10)
obj.add_menu_item("Coffee", 15)
obj.add_menu_item("Lime Juice", 20)
obj.add_menu_item("French Lime", 20)
obj.add_menu_item("Apple Juice", 80)

obj.print_menu()

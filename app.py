class Shop:
    def __init__(self, name, location, inventory):
        self.name = name 
        self.location = location 
        self._inventory = inventory  

    def display_details(self):
        return f"Shop Name: {self.name}, Location: {self.location}"

    def check_stock(self, item):
        return self._inventory.get(item, 0)

    def add_stock(self, item, quantity):
        if item in self._inventory:
            self._inventory[item] += quantity
        else:
            self._inventory[item] = quantity

class OnlineShop(Shop):
    def __init__(self, name, website, inventory):
        super().__init__(name, "Online", inventory)
        self.website = website 

    def display_details(self):
        return f"Online Shop Name: {self.name}, Website: {self.website}"

shop = Shop("Local Market", "Downtown", {"Apples": 50, "Oranges": 30})
print(shop.display_details()) 
print(f"Apples in stock: {shop.check_stock('Apples')}")  

online_shop = OnlineShop("E-Shop", "www.eshop.com", {"Laptops": 20, "Phones": 10})
print(online_shop.display_details())  
print(f"Laptops in stock: {online_shop.check_s


#2
class Vehicle:
    def move(self):
        pass  

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

def show_movement(vehicle):
    print(vehicle.move())

car = Car()
plane = Plane()
boat = Boat()

show_movement(car) 
show_movement(plane)
show_movement(boat)  

class Restaurant():
    def __init__(self, restaurant_name, 
                cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant is " + self.restaurant_name + 
        " and the cuisine is " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, 
                cuisine_type):
        super().__init__(restaurant_name, 
                    cuisine_type)
        self.flavours = ['Vanilla', 'Chocolate',
                        'Strawberry']
    
    def display_flavours(self):
        print("The flavours are:")
        for flavour in self.flavours:
            print(flavour)

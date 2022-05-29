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

restaurant = Restaurant('Saffron', 'Butter Chicken')
print(restaurant.number_served)

restaurant.number_served = 2
print(restaurant.number_served)

restaurant.set_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)
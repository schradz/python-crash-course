class cRestaurant:
    """A simple  attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.is_open = False

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine} style restaurant")

    def open_restaurant(self):
        self.is_open = True
        print(f"{self.name} is now open!")

    def close_restaurant(self):
        self.is_open = False
        print(f"{self.name} is now closed!")

    def get_open_status(self):
        if self.is_open == True:
            print(f"{self.name} is open!")
        elif self.is_open == False:
            print(f"{self.name} is closed!")

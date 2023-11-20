"""Defining a Class!"""

"""
Think of a class definition as a "roadmap" for objects that belong to the class
You are defining the underlying structure every instance of this class will have
"""

class Pizza:

    #attributes
    # Think of these as the variables
    # each instance of my class will have <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """My constructor"""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf
        # returns a Pizza object
    
    def price(self) -> float:
        """Calculate price of pizza"""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.glutten_free:
            price += 1.00
        return price 
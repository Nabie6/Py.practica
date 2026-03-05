class Car:
    def __init__ (self, color, wheel, type, price):
        self.color=color
        self.wheel=wheel
        self.type=type
        self.price=price

bmw=Car("Red", 4, "X5", "98k$")

print(bmw.type)
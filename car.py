class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.p_speed = 0

    def accelerate(self):
        self.p_speed += 10

    def brake(self):
        self.p_speed -= 10

    def get_speed(self):
        return self.p_speed
    
car1 = Car("BMW", "BLUE")

car1.accelerate()
car1.accelerate()
car1.brake()
print(car1.get_speed())

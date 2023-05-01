class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Animal's speak")

animal1 = Animal("동물", 0)
animal1.speak()

class Dog(Animal):
    def speak(self):
        print("강아지는 멍멍")

class Cat(Animal):
    def speak(self):
        print("고양이는 야옹야옹")

dog1 = Dog("위니", 4)
cat1 = Cat("두부", 3)

dog1.speak()
cat1.speak()
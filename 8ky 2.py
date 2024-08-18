class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
class Animal:
    def __init__(self, name):
        self.name = name   
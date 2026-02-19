class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.breathe()
my_dog.bark()
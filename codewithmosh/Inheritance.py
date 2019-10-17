class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")
    # pass


class Cat(Mammal):
    def be_annoying(self):
        print("Cat is annoying")
    # pass


dog1 = Dog()
dog1.walk()
dog1.bark()
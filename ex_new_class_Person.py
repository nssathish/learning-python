class Person:
    def __init__(self, name):
        self.name = name

    def talk(self, name):
        print(f"{self.name} is talking to {name}")


person = Person("Sathish")
person.talk("Seethu")
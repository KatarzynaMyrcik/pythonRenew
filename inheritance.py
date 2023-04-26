#inheritance
class Mammal:
    def __init__(self, name):
        self.name = name
        print(name)


    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} is barkig")


class Cat(Mammal):
    def be_annoying(self):
        print("I'm annoying Catik")


Fafik = Dog("Fafik")
Fafik.walk()
Fafik.bark()
Kitik = Cat("Kitik")
Kitik.be_annoying()
Kitik.name

'''result:
Fafik
walk
Fafik is barkig
Kitik
I'm annoying Catik
'''

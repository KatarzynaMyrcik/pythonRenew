class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print(f"dog is barkig")


class Cat(Mammal):
    def be_annoying(self):
        print("I'm annoying Catik")


Fafik = Dog()
Fafik.walk()
Fafik.bark()
Kitik = Cat()
Kitik.be_annoying()


'''result:
walk
Fafik is barkig
I'm annoying Catik
'''

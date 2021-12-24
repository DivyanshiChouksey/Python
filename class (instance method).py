# class (instance method)
class Person:
    def __init__(self):
        self.name = input("Enter name ")
        self.age = int(input("age "))
    def talk(self):
        print(self.name,self.age)

P1 = Person()
P1.talk()

P2 = Person()
P2.talk()

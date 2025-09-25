class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

class Employee(Person):
    pass

Pr = Person("nihal",20)
Pr.display()
Ep = Employee("Nishant",25)
Ep.display()
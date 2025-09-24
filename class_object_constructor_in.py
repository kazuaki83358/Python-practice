class MyClass:
    x = 5
#creating object to access element from myclass
mc = MyClass()
print(mc.x)

class Person:
    #permeterised constructor in python
    def __init__(self,name,age):
        self.name = name
        self.age = age
#providing value toh constructor 
pr = Person("Nishant Kumar",21)
print(pr.name)
print(pr.age)



def add(a=5, b=6):
    return a + b


print(add())
print(add(10))
print(add(10, 20))


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)


result = average(12, 5, 3, 7, 5)
print(result)


def name(**name):
    print("Hello", name["fname"], name["mname"], name["lname"])


name(fname="Nishant", mname="Kumar", lname="Singh")

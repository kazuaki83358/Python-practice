def greeting(fn):
    def wrapper():
        print("Good Morning")
        print(fn().upper())
        print("Nice to meet you")
    return wrapper   # ✅ return the wrapper

@greeting
def result():
    return "nishant kumar"

result()

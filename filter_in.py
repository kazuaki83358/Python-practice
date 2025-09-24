def start_a(w):
    return w.startswith("a")

li = ["apple", "mango", "avocado", "apricot", "cherry"]
#filter everything which start from a and store here
result = filter(start_a,li)
print(list(result))
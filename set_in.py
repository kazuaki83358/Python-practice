SetOfData = {"nishant", "nihal", "nikhil", "nikhil", "adnan"}
SetIfDiffData = {"nandini", "nikita", "nishant", "nikhil"}

# It's remove duplicate data from set
print(SetOfData)
# It's provide intersection between 2 data and common data is returned
print(SetIfDiffData.intersection(SetOfData))
# It's provide which data is different from another set with another set we are comparing with
print(SetOfData.difference(SetIfDiffData))
SetOfData.update(SetIfDiffData)
print(SetOfData)
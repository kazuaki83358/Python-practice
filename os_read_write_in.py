import os

file_path = "try.txt"
with open(file_path, 'w') as f:
    f.write("hello this is my first txt file writing using python")

os.mkdir('Api_calling')

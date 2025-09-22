import os

# It will print current working direcotry 
print("Current directory: ", os.getcwd())
# It will create .txt file if do not exist and write in it
file_path = "try.txt"
with open(file_path, 'w') as f:
    f.write("hello this is my first txt file writing using python")

os.mkdir('Api_calling')
# It will list all the files in current directory 
print(os.listdir("."))

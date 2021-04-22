import os

# URL Documentation about module os https://www.geeksforgeeks.org/os-module-python-examples/

myDirectory = os.getcwd()
print("Directorio actual: " + str(myDirectory))

newDirectory = "NewDirectory"

path = os.path.join(myDirectory, newDirectory)

# os.mkdir(path)

# os.rmdir(path)

userLogged = os.getlogin()
print(userLogged)
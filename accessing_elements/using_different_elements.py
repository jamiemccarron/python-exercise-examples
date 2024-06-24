# Dictionary
dictionaryElement = {"key1":"Hello", "key2":"World!"}

# List
listElement = ["Hello", "World!"]

# Funtion with a return string
def my_function ():
    return "I'm the string that will be returned from my_function"

# Class
class MyClass:
    def __init__ (self):
        self.myStringVariable = "I'm a class variable string"

    def my_class_function (self):
        return "From Class Function: " + self.myStringVariable

    @staticmethod
    def add (x,y):
        return x + y

# Add to the following print, the combined dictionary string to say Hello World!
print (dictionaryElement["key1"], dictionaryElement["key2"])
# Add to the following print, the combined list to say Hello World!
print(" ".join(listElement))

# Add to the following print, the function to print out its return string
print(my_function())

# Declaring the class
A = MyClass()

result=A.add(1,2)
print(result)
# Add to the following print, the class variable myStringVariable
print(A.myStringVariable)

# Add to the following print, the class function to print out its return string
print (A.my_class_function())



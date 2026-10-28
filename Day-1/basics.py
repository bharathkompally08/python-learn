## printing
# print("hello", "world", "run") 

## printing with seperator add a seperator between texts
# print("hello", "my", "world", sep= "-")

## end in print
# print("hello", end= " ")
# print("world")


## files
# f = open("output.txt", "w")
# f.write("hello-world")
# f.close()

# with open("output.txt", "w") as f:
#     print("hello", file= f)

# import time

# print("Hello", end="")
# time.sleep(5)

# print(" World")


# variables
# x = 10
# print(x)
# x= 20
# print(x)

# data types
# x = 4 
# print(type(x)) ##<class 'int'>

# x= 2.2
# print(type(x)) ## <class 'float'>

# x = "str"
# print(type(x)) ## <class 'str'>

# x= ["1", 2.2, ["str", "ind"]]
# print(type(x)) ## <class 'list'>

# x = {
#     "name" : 1,
#     "age" : 20
# }
# print(x, type(x)) ## {'name': 1, 'age': 20} <class 'dict'>

# print(0.1 + 0.2) ## 0.30000000000000004
# x= True
# y =False
# print(type(x), type(y)) ##<class 'bool'> <class 'bool'>

# print(x + y)

# x = None
# print(x, type(x)) ## None <class 'NoneType'>

## type conversions
# x = 2.2
# y =int(x)
# print(type(x), type(y)) ## <class 'float'> <class 'int'>

x = "indian"
y = 2
# print(x + y) ## TypeError: can only concatenate str (not "int") to str
# print(int(x) + y) ## ValueError: invalid literal for int() with base 10: 'indian'
# print(x + str(y)) ##  indian2

## string convert to int ?? -> text strings cannot be converted to int only any values with strings are converted to int
# print(int("12.2")) ## ValueError: invalid literal for int() with base 10: '12.2'
# print(int(float("12.2"))) ## 12
# name = "aryan"
# age = 20
# print(f"My name is {name} and my age is {age}")

##input
# x = input("Provide input: ")
# print(f"your input is {x}, and type is {type(x)}")


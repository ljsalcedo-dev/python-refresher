# a variable is created once you assign a value to it

x = 1 # int type
y = "Lance" #str type
print(x) # or y

# type casting = changing one type to another

myInt = 4 # int type variable
myString = str(myInt) # int to str
print(type(myString)) # we can get the type using type() function; this outputs "<class='str'>"

# variable names are case sensitive

a = 1 # a's value is 1
A = 4 # A will not overwrite a since they are different variables
print(a, A) # outputs "1 4"

# variable naming rules

# 1) MUST START with a LETTER or UNDERSCORE '_'
b = 4
_ = 1
print(_) # outputs "1"

# 2) CANNOT START with a NUMBER
# 1number = 444 # syntax error
# print(1number)

# 3) variable names can only contain ALPHA-NUMERIC characters AND UNDERSCORES (A-Z a-z 0-9 _)
myGreeting = "Welcome"
# myGreeting! = "Welcome!" # syntax error

# 4) variable names cannot be any of the Python keywords
# class = "This is my class" # syntax error; class is a reserved keyword

# three naming conventions for variable names

# 1) camel case
myVariableName = "This is a variable" # this is the one i prefer the most

# 2) pascal case
MyVariableName = "This is another variable"

# 3) snake case
my_variable_name = "You can also do this for a variable"

# assigning values

# multiple values to multiple variables
j, k, l = 1, 2, 3
"""
this is like
j = 1
k = 2
l = 3
but with one line
"""
print(j, k, l) # outputs "1 2 3"

# one value to multiple variables
j = k = l = 4
print(j, k, l) # outputs "4 4 4"

# global variables

# created outside of a function
myGlobalVariable = "Lance"

def myFunction():
    print("My name is", myGlobalVariable)

myFunction()

# using the global keyword

def MyFunction():
    global MyGlobalVariable
    MyGlobalVariable = "This is also a global variable"

MyFunction()

print(MyGlobalVariable)
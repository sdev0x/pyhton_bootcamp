#      - Defining and calling void function.
def welcome():
    print("hello")
welcome()
#      - Parameters + return value
def welcome(name):
 return name

x = welcome('sari')
print(x)

print(welcome("lama"))
#      - Local and Global variables
def sum(num1 , num2):
    global number
    number = 5
    print(number)
    print(num1 + number)
sum(1 , 3)
print(number)
#      - Function chaining.
name = ' sari '
print(name.upper().lower())
x = name.upper()
print(x.lower())

myStr = "Hello World"


result = myStr.upper().replace("HELLO", "hi").lower()
print(result)

result = myStr.upper().replace("HELLO", "Hi").count("l".upper())
print(result)
#      - Positional arguments
def sum(num1 , num2):
    print("num1 = ",num1)
    print("num2 =",num2)
    print(num1 + num2)
sum(6 , 7)

def multiply(num1,num2,num3):
    print(num1 * num2 *num3)
multiply(4,2,5)
#Default arguments

def information(name='ahmed',age=12):

    print("name is",name)
    print('age is',age)
information('lama',20)
information('sari')
information()

#     - Keyword arguments
sum(num2 = 10,num1 = 2)
# sum(num4 = 10,num3 = 5)
sum(1,3)
# Using keyword arguments



# Argument Packing


# Argument Unpacking

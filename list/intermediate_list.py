names = ["sari","khalid"]
for name in names:
    print(name)
def capitalize(name):
    return name.upper()

capitalized = list(map(capitalize, names))
capitalized = map(capitalize , names)
print(list(capitalized))
print(names)
#filter function
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = filter(is_even,numbers)
print(list(even_number))


def is_uppercase(string):
    return string.isupper()

strings = ["HELLO", "world", "PYTHON", "programming"]
uppercase = filter(is_uppercase , strings)
print(list(uppercase))

def is_positive(number):
    return number > 0
num= [-3, -2, -1, 0, 1, 2, 3]
positive = filter(is_positive , num)
print(list(positive))

my_dict = {'name': 'Sari', 'age': 11}
print(my_dict["name"])
my_dict['age'] = 12
print(my_dict['age'])
my_dict['city'] = "riyadh"
print(my_dict)
dict = {}
dict['name']='lama'
print(dict)
# Using kes() method to g et the keys of the dictionary
print(my_dict.keys())
# Using valu es() method to get the values of the dictionary
print(my_dict.values())
# Using items() method to get the key-value pairs of the dictionary
print(my_dict.items())

#  - Nested dictionary
my_dict = {
            'dict1':{'name': 'Sari', 'age': 11},
           'dict2':{'name': 'ahmad', 'age': 11}
           }
print(my_dict.keys())
print(my_dict['dict1'].keys())


# print an element in the dictionary
print(my_dict['dict2']['name'])
print(my_dict['dict2'])
print(my_dict['dict1']['age'])
# Update the age of the person3


my_dict['dict1']['age']=12
print(my_dict)

my_dict['dict2']['name']='khalid'
print(my_dict)
# add new element to the dictionary
my_dict['dict3']={'name':'lama','age':10}
print(my_dict)
# print all elements in the dictionary

for key,value in my_dict.items():
    print(f"key:{key},value:{value}")


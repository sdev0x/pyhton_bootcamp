# Tuple ()

# List []
# Dictionary {}

#  4. Tuples
#   - Creating a Tuples.
tuplee = ("A","B","A","D")

# Print the letter 'A' from the tuple.
print(tuplee[0])

#   - Checking membership.
if "A" in tuplee:
    print("A")

#   - Finding the length of a tuple.
print(len(tuplee))
#   - Slicing tuples.
print(tuplee[0:3])
print(tuplee[slice(0,4)])
#   - Tuple methods (index, count)
print(tuplee.index("A"))
print(tuplee.count("A"))
#   - Converting tuples to lists.
# mylist = list(tuplee)
# print(mylist)
user = int(input("enter a number"))
print(user + 2)
#  Converting tuples to lists using extend method.
mylist = []
mylist.extend(tuplee)
print(mylist)

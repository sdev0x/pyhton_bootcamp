# #List comprehension
# numbers = [1, 2, 3, 4, 5]
#
# # Square each number using list comprehension
# squared_numbers = [x ** 2 for x in numbers]
# print(squared_numbers)
#
# even_number = [x for x in numbers if x % 2 == 0]
# print(even_number)
#
# # upper = [s for s in strings if s.isupper()]
# upper = [s.upper() for s in strings ]
# print(upper)
# - 2D Lists <-

twoDList = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90],
            [10 , 20 , 30]]

# print 2D list
# print(twoDList)

# - Print 2D List using for loop
for row in twoDList:
    for element in row:
        print(element)
    print()
# add element to 2D list

twoDList.append([1,2,3])
twoDList.insert(0, [100, 110, 120])
print(twoDList)
get element from 2D list
print(twoDList[1][2])
print(twoDList[2][0])

#update element
print(twoDList[4][2])
twoDList[4][2] = 30
print(twoDList[4][2])
len
print(len(twoDList))
print(len(twoDList[2]))

# # find element in 2D list
target = 50
for row in range(len(twoDList)):
    for coulmn in range(len(twoDList[row])):
        if twoDList[row][coulmn] == target:
            print(f"Element {target} found at position ({row}, {coulmn})")

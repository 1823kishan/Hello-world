# Python program to find sum of elements in list

# total = 0
# list1 = [11, 5, 17, 18, 23]
# for ele in range(0, len(list1)):
#     total = total + list1[ele]
#
# print("Sum of all elements in given list: ", total)


# multiply list value----------------------------------------------

# list2 = [1, 2, 3]
# total = 1
# for i in list2:
#     total *= i
# print(total)


# print largest number------------------------------

# list1 = [12, 67, 89, 77, 90]
#
#
# print(max(list1))


# print smallest number----------------------------

# list1 = [12, 90, 78, 6]
# print(min(list1))


# print same name second lenght--------------------

# list1 = ["kishan", "c", "savaliya", "c"]
#
# print(list1.index("c", 3))


# print sorted element---------------------------------

# list1 = [23, 87, 4, 78, 9]
#
#
# list1.sort()
# print(list1)


# print to duplicate delete--------------------------------------

# list1 = [1, 8, 1, 8, 7]
#
# print(list(set(list1)))


# print list is empty or not---------------------

# list1 = [0, ]
# for i in list1:
#     if list1 == None:
#         print("list is empty")
#         break
#     else:
#         print("list is not empty")
#         break


# print copy list--------------------------------------

# list1 = [1, 2, 3]
#
# list2 = list1.copy()
#
# print(list2)


# print same items in list-------------------------------------

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# result = False
# for x in list1:
#     for y in list2:
#         if x == y:
#             result = True
#             print(result)


# print to delet item output shoud it------------------

# SampleList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
# SampleList.pop(5)
# SampleList.pop(4)
# SampleList.pop(0)
# print(SampleList)


# print specified value after removing even number---------------

# num = [7, 8, 120, 25, 44, 20, 27]
# num = [x for x in num if x % 2 != 0]
# print(num)


# print list items square-------------
list1 = []

for i in range(1, 31):
    list1.append(i ** 2)
print(list1)


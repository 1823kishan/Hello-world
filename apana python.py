'''
# type convertion
#old_age = input("enter your old age: ")
new_age = int(old_age) + 2
#print(new_age)

#first = input("enter first number: ")
#second = input("enter second number")

sum = int(first) + int(second)
print("sum of two number is:", sum)
'''

# string
'''
name = "Tony stark"
print(name.upper())
print(name.lower())
print(name.find('s'))
print(name.replace("stark", "Iron man"))
print('T' in name)
'''

# Arithmetic operator
'''
print(5+2)
print(5%2)  #aa ee ses avase.
print(5**2) #aa ee varg karava mate.
print(5**3)
print(125*5)
i = 5
#i = i + 2
i += 2
print(i)
'''

'''
# ---------- OPERATOR PRECEDENCE-------------
result = 2+3*5  # ama pela je opreation lese te ne pela operat karase.
print(result)
'''
'''
# Comparison operators
print(3>2)
print(3<2)
print(3>=2)
print(3==2)
print(3!=2)
'''

'''
# Logical operator
print(2 > 3 or 2 > 1)
print(3 > 2 and 2 > 6)
print((not 2 > 3))
'''
'''
# if-else statment
age = 2
if age >= 18:
    print("ypu are an adult")
    print("you can vote")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("you are a child")
'''
'''
# MINI PROJRCT OF MAKE A CALCULATER.
first = input("enter first number : ")
operator = input("enter operator you want (+, -, *,  /, %)=>")
second = input("enter second number: ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("in valid operator")
'''

# Range
#numbers = range(5)
#print(numbers)


#------loop-------
'''
# while loop
i = 5
while i >= 1:
    print(i * "*")
    i = i - 1
'''
'''
# For loop
for i in range(5):
    print(i + 1)
'''
'''
# List
marks = [95, 86, 87, "maths"]
#print(marks[0])
#print(marks[0:2])
#for score in marks:
    #print(score)
marks.append(99)
print(marks)
marks.insert(0, 99)
print(99 in marks)
print(len(marks))
print(marks)
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
marks.clear()
print(marks)
'''
'''
# Break & countinua

student = ["ram", "shyam", "kishan", "radha", "radhika"]
for student in student:
    if student == "radha":
        break
    print(student)

student = ["ram", "shyam", "kishan", "radha", "radhika"]
for student in student:
    if student == "kishan":
        continue
    print(student)
'''
'''
# Tuple. it is imutable.
# ama ()aa comlsary nathi hota.
tuple = (12, 77, 77, 12, 88, 77)
print(tuple.count(12))
print(tuple.index(77))
'''
'''
#set
set = {22, 54, 87, 98, 7, 7, 7}
print(set)
'''
'''
# Dictionary
marks = {"english": 95, "chemestry": 98}
print(marks)
print(marks["chemestry"])
marks["physics"] = 97
print(marks)
marks["physics"] = 99
print(marks)
'''

# Function
# their are three types of function
#in-built, module, user-defined.
def print_sum(first, second=4):
    print(first + second)
print_sum(1, 2)

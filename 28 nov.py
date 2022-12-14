# a=int(input("Enter your first value::"))
# b=int(input("Enter your 2nd value::"))
# c=a+b
# print("C:",c)


# def add_two():
#     a=int(input("Enter your first value::"))
#     b=int(input("Enter your 2nd value::"))
#     print(a+b)

# add_two()
# add_two()



# def add_two():
#     a=int(input("Enter your first value::"))
#     b=int(input("Enter your 2nd value::"))
#     return a+b,a-b

# c=add_two()
# f=add_two()
# print(c)
# print(f)


# def add_two(a,b):
#     return a+b
# a=int(input("Enter your first value::"))
# b=int(input("Enter your 2nd value::"))
# print(add_two(a,b))
# print(add_two("Chirag","Joshi"))
# print(add_two(10,40))



# def last_char(name):
#     return name[-1]

# user_name=input("Enter your name:::::")
# print(last_char(user_name))


# def  odd_even(num=int(input("enter your num:"))):
#     if num%2==0:
#         return "odd"
#     else:
#         return "Even"
# print(odd_even())

# def  is_even(num=int(input("enter your num:"))):
#     if num%2==0:
#         return True
#     else:
#         return False
# print(is_even())



# def greter(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(greter(60,500))


# def gretest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(gretest(100,500,32))


# function inside function
# def gretest (a,b,c):
#     temp=greter(a,b)
#     return greter(temp,c)
# print(gretest(100,500,32))

# def gretest (a,b,c):
#     temp=greter(a,b)
#     return temp*c
# print(gretest(10,45,3))



# default parameter

def user_info(name='unknow',age=None):
    return f"your name is {name} your age is {age}"

print(user_info())


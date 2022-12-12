# polymorphism  method overloading

# class VIP:
#     def vsp(self, x=None, y=None):
#         if x == None and y == None:
#             print("this is polymorphism")
#         elif x != None and y == None:
#             f = 1
#             for i in range(1, x + 1):
#                 f = f * i
#             print("factorial is::", f)
#         else:
#             print("addition is ::", (x + y))
#
#
# ob = VIP()
# ob.vsp()
# ob.vsp(5)
# ob.vsp(16, 14)

# method overriding------------------------------------------------

# class A:
#     def vsp(self):
#         print("hi")
#
#
# class B:
#     def vsp(self):
#         print("hello")
#
#     def xyz(self):
#         print("tata bye")
#
#
# ob = B()
# ob.vsp()
# ob.xyz()

# operatoer overloading--------------------------------------

class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, o):
        return self.x + o.x


o1 = A(20)
o2 = A(20)

print(o1 + o2)

# class MyClass:
#     def fun(self, x):
#         f = 1
#         for i in range(1, x + 1):
#             f = f * i
#         print(f)
#
#
# ob = MyClass()
# a = int(input("enter your number"))
# ob.fun(a)


#--------------------------------------------------------------------
#STUDENT DETAIL

class Student_record:
    def student_detail(self, name, rl, cl):
        print("name of student", name)
        print("roll of student", rl)
        print("class of student", cl)
    def student_mark(self, marks, per, gr):
        print(marks)
        print(per)
        print(gr)



ob = Student_record()

ob.student_detail("kishan savaliya", 101, "C")
ob.student_mark(470, 75, "B")

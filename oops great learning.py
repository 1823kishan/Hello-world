class emp:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_emp_details(self):
        print('emp name is', self.name)
        print('emp age is', self.age)
        print('emp salary is', self.salary)
        print('emp gender is', self.gender)

e1 = emp('ram', 32, 50000, 'male')
e1.show_emp_details()

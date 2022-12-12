class Pattern:
    def star1(self):
        n = int(input("enter your number"))
        for i in range(1, n):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    def star2(self):
        n = int(input("enter your number"))
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()

    def abc(self):
        for i in range(0, 5):
            for j in range(1):
                print("A", end=" ")
                print("B", end=" ")
                print("C", end=" ")
                print("D", end=" ")
            print()


ob = Pattern()
# ob.star()
# ob.star2()
# ob.abc()
# ob.abc()

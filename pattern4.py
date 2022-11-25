for i in range(5, 0, -1):
    for _ in range(5, i, -1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
    
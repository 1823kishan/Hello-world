for i in range(1, 6):   # (5, 0, -1) if you want to recers.
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

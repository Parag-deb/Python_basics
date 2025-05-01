def fancy_star(n=7):
    print("Fancy Star-Diamond:\n")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        print("*", end="")

        if i != 0:
            for j in range(2 * i - 1):
                print(" ", end="")
            print("*")
        else:
            print()

    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        print("*", end="")

        if i != 0:
            for j in range(2 * i - 1):
                print(" ", end="")
            print("*")
        else:
            print()

fancy_star()

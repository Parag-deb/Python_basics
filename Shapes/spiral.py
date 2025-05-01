def draw_spiral(size=10):
    for y in range(size):
        for x in range(size):
            if (x == y) or (x + y == size - 1):  # Diagonal lines
                print("*", end="")
            else:
                print(" ", end="")
        print()

draw_spiral(20)

def print_x(n):
    print("\nX Shape:")
    for i in range(n):
        for j in range(n):
            if i == j or j == n - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_y(n):
    print("\nY Shape:")
    for i in range(n):
        for j in range(n):
            if (i <= n // 2 and (j == i or j == n - 1 - i)) or (i > n // 2 and j == n // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_triangle(n):
    print("\nTriangle Shape:")
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

def print_heart():
    print("\nLove (Heart) Shape:")
    for row in range(6):
        for col in range(7):
            if ((row == 0 and col % 3 != 0) or 
                (row == 1 and col % 3 == 0) or 
                (row == 2) or 
                (row - col == 2) or 
                (row + col == 8)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Set size for shapes
size = 7

# Call the functions
print_x(size)
print_y(size)
print_triangle(size)
print_heart()

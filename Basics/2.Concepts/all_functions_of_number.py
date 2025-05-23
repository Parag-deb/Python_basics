# number_basics.py
import math
import random
# Integers
x = 10
print(f"1. Integer: {x}")  # 10

# Float
y = 3.14
print(f"2. Float: {y}")  # 3.14

# Complex numbers
z = 2 + 3j
print(f"3. Complex: {z}")  # (2+3j)

# Type checking
print(f"4. Type of x: {type(x)}")  # <class 'int'>

# Type conversion
a = float(x)
print(f"5. Convert int to float: {a}")  # 10.0

b = int(y)
print(f"6. Convert float to int: {b}")  # 3


# abs()
print(f"1. abs(-5): {abs(-5)}")  # 5

# pow()
print(f"2. pow(2, 3): {pow(2, 3)}")  # 8

# divmod()
print(f"3. divmod(10, 3): {divmod(10, 3)}")  # (3, 1)

# round()
print(f"4. round(3.456): {round(3.456)}")  # 3

# round() with ndigits
print(f"5. round(3.456, 2): {round(3.456, 2)}")  # 3.46

print(f"1. math.ceil(3.1): {math.ceil(3.1)}")  # 4
print(f"2. math.floor(3.9): {math.floor(3.9)}")  # 3
print(f"3. math.sqrt(16): {math.sqrt(16)}")  # 4.0
print(f"4. math.factorial(5): {math.factorial(5)}")  # 120
print(f"5. math.fabs(-5): {math.fabs(-5)}")  # 5.0


print(f"1. math.log(100, 10): {math.log(100, 10)}")  # 2.0
print(f"2. math.exp(2): {math.exp(2)}")  # ~7.389
print(f"3. math.sin(math.pi/2): {math.sin(math.pi/2)}")  # 1.0
print(f"4. math.cos(0): {math.cos(0)}")  # 1.0
print(f"5. math.tan(math.pi/4): {math.tan(math.pi/4)}")  # ~1.0


print(f"1. random.randint(1, 10): {random.randint(1, 10)}")  # Random int between 1 and 10
print(f"2. random.random(): {random.random()}")  # Float between 0 and 1
print(f"3. random.uniform(1.5, 4.5): {random.uniform(1.5, 4.5)}")  # Float between 1.5 and 4.5

# Number testing
print(f"4. isinstance(10, int): {isinstance(10, int)}")  # True
print(f"5. isinstance(3.5, float): {isinstance(3.5, float)}")  # True
def print_bow_and_arrow(width=15):
    print("Bow and Arrow Shape:\n")
    
    # Drawing the bow
    for i in range(width):
        print(" " * (width - i - 1) + "*" * (2 * i + 1))

    # Arrow shaft
    for i in range(width // 3):
        print(" " * (width // 2) + "|")

    # Arrowhead
    for i in range(width // 3):
        print(" " * (width // 2 - i) + "*" * (2 * i + 1))

print_bow_and_arrow()

import math

def horizontal_crescent_moon():
    radius = 8  # Radius of the main circle (the moon)
    cut_radius = 6  # Radius of the cut-out circle (the shadow area)
    
    # Adjust the width and height for a more proportional moon shape
    width = radius * 2
    height = radius
    
    for y in range(-height, height + 1):
        for x in range(-width, width + 1):
            # Distance from the center for the main circle
            distance1 = math.sqrt(x**2 + y**2)
            # Distance from the center for the cut-out (second) circle
            distance2 = math.sqrt((x - 3)**2 + y**2)  # Shifted slightly to the right
            
            # Check if the point (x, y) lies within the main circle but outside the cut-out circle
            if distance1 <= radius and distance2 > cut_radius:
                print("*", end="")
            else:
                print(" ", end="")
        print()

horizontal_crescent_moon()

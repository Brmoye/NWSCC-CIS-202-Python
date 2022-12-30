import math

area = float(input("Enter the area of a circle: "))
if area > 0:
    radius = math.sqrt(area / math.pi)
    print("The radius is", radius)
else:
    print("ERROR: The area must be a positive number.")

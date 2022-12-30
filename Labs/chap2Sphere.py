"""
Program: chap2Sphere
Author: Brian Moye
Puprose: Based on user input, this program will calculate a sphere's
         diameter, circumference, surface area, and volume.
"""

from math import pi

#Get radius from user
radius = float(input("Enter a sphere radius: "))
radius = 3
#Calculate the sphere's diameter, circumference, surface area, and volume.
diameter = 2 * radius                       #calculate diameter
circum = 2 * pi * radius                    #calculate circumference
surfaceArea = 4 * pi * radius ** 2          #calculate surface area
volume = (4.0 / 3.0) * pi * radius ** 3     #calculate volume

#Display results to user
print("\nSphere Properties")
print("-----------------")
print("Diameter:", round(diameter, 2))
print("Circumference:", round(circum, 2))
print("Surface Area:", round(surfaceArea, 2))
print("Volume:", round(volume, 2))

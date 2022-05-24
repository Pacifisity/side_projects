import math

height = int(input("Pool Height in inches:\n"))
radius = int(input("Pool Radius in inches:\n"))
pi = math.pi

def chicken_dick_shape_calculator(height, radius):
    volume = pi * (radius ** 2) * height
    return volume

volume = chicken_dick_shape_calculator(height, radius)
circumference = 2 * pi * radius

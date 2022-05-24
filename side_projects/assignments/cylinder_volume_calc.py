import random
height_input = random.randint(1,50)
raidius_input = random.randint(1,20)

# Write a program to calculate the volume of a cylinder.
# You will do this by writing a custom function that accepts the radius and height as inputs and returns the volume.
# In this case, it does not make sense to set any default values for your inputs.
# You should import the math module and use the constant pi by typing math.pi.
# In your main program, outside of your function, use your function to calculate the volume of cylinders with radius of 2 and height of 0.4, and radius of 3.1 and height of 2.
# In each case, your program prints the resulting volume.
import math                                                                        # import the math API wrapper

height = height_input                                                              # input height and then save it in a variable
radius = raidius_input                                                             # input radius and then save it in a variable
pi = math.pi                                                                       # pi value holder
def chicken_dick_shape_calculator(height, radius):                                           # function
    volume = pi * (radius ** 2) * height                                           # cylinder volume formula
    return volume                                                                  # returns the value of volume

volume = chicken_dick_shape_calculator(height, radius)

print(volume)
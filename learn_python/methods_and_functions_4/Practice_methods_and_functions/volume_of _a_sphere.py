#Write a function that computes the volume of a sphere given its radius.
#example: vol(2) -> output:33.510321638291124
#Volume of the sphere: (4*pi*R**3)/3

from math import pi
def vol(rad):
    return (4*pi*rad**3)/3
print(vol(2))
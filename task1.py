import math # use math.pi from this module

# Function for calculation of volume of a cylinder 


def calculate(R, L):
    volume = math.pi * R * R * L
    return ('Volume: ' +  str(volume))
R = int(input('Enter radius: '))
L = int(input('Enter length: '))

print(calculate(R, L))

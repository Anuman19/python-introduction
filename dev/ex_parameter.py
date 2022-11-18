#!/usr/bin/python3

import math

def radius(r):
    return round(r * 2 * math.pi, 1)


def area(r):
    return round(r**2 * math.pi, 1)


def volume(r, h=10):
    return round(r**2 * math.pi * h, 1)

"""
r = int(input("radius: "))
#h = int(input("height: "))

print(radius(r))

print(area(r))

print(volume(r))
"""
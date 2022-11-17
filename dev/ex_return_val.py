#!/usr/bin/python3

from ex_parameter import area, radius, volume

def circle(r):
    return area(r), radius(r), volume(r)

print(__name__)

if __name__ == "__main__":
    a, c, v = circle(3)
    print("area:", a)
    print("cirumference:", c)
    print("volume:", v)

    x = circle(3)
    print("area-tuple:", x[0])
    print("ciru-tuple:", x[1])

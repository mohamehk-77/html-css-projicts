from math import pi

def circle_area(r):
    return pi*(r**2)

#test func

radll = [2, 0, -3, 2 + j5, True, "radius"]

masg = "Area circle with r = {radius} is {area}."

for r in radll:
    A = circle_area(r)
    print(masg.format(radius=r, area=A))
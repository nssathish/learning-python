from collections import namedtuple

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#if it is just a data calse
#we can use namedtuple
Point = namedtuple("Point", ["x", "y"])

point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1)
print(point1 == point2)
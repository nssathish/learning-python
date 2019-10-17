class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # if there are 2 init constructors
    # The latest one is picked up since
    # python has the top down approach
    #
    # This is interesting

    # def __init__(self):
    #     self.x = 10
    #     self.y = 20

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point = Point(30,40)
print(str(point.x) + ',' + str(point.y))

point.x = 10
point.y = 20

point.draw()
point.move()

print(str(point.x) + ',' + str(point.y))

# point1 = Point()
# print(str(point1.x) + ',' + str(point1.y)) # run time error: instance doesn't have the attributes x,y

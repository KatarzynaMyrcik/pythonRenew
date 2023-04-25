class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point2 = Point()
point1.x = 1
point2.y = 2
point1.draw()
print(point2.y, point1.x)

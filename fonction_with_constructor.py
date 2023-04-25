class Point:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #fonction
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#how to use constructor
point1 = Point(10, 20)
print(point1.x)

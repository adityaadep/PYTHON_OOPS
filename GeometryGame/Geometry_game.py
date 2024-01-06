from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if(rectangle.point1.x < self.x < rectangle.point2.x
                and rectangle.point1.y < self.y < rectangle.point2.y):
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas, size=5, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size,color)


rectanglex = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(0, 400),
                                                                         randint(10, 400)))


print("Rectangle coordinates:",
      rectanglex.point1.x, ",",
      rectanglex.point1.y, ",",
      rectanglex.point2.x, ",",
      rectanglex.point2.y, ",",
)

# get point and area from user
user_input = GuiPoint(float(input("Guess X : ")), float(input("Guess Y: ")))

user_area = float(input("Guess area: "))

if user_input.falls_in_rectangle(rectanglex):
    print("Your point was inside rectangle")
else:
    print("Your point was not inside rectangle")

print("Your Guessed area", user_area)
print("Actuall area", rectanglex.area())

myturtle = turtle.Turtle()
rectanglex.draw(myturtle)
user_input.draw(myturtle)
turtle.done()



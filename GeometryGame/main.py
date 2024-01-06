import turtle

# create a canvas instance
myturtle = turtle.Turtle()

# penup will hide the pen
myturtle.penup()
myturtle.goto(50,75)

# pendown will write and get unhidden
myturtle.pendown()
# move 100 pixels forward
myturtle.forward(100)

# turn 90 degrees left
myturtle.right(90)
myturtle.forward(100)

myturtle.right(90)
myturtle.forward(100)

myturtle.right(90)
myturtle.forward(100)

turtle.done()


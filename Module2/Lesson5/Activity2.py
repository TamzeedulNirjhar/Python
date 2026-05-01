import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,400)
star = turtle.Turtle()

#1st triangle
star.forward(100)
star.left(120)
star.forward(100)
star.left(120)
star.forward(100)
star.penup()
star.right(150)
star.forward(50)

#2nd triangle
star.pendown()
star.right(90)
star.forward(100)

star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

turtle.done()


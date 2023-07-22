import turtle

turtle.speed(0)

# front rectangle
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

turtle.penup()
turtle.goto(100, 50)
turtle.pendown()

# back rectangle
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# top left line
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(100, 50)

# bottom left line
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.goto(100, -50)

# top right line
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.goto(300, 50)

# bottom right line
turtle.penup()
turtle.goto(200, -100)
turtle.pendown()
turtle.goto(300, -50)

turtle.hideturtle()
turtle.done()

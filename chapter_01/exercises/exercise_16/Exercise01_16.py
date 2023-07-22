import turtle

# top left circle
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.circle(100)

# top right circle
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(100)

# bottom left circle
turtle.penup()
turtle.goto(-100, -200)
turtle.pendown()
turtle.circle(100)

# bottom right circle
turtle.penup()
turtle.goto(100, -200)
turtle.pendown()
turtle.circle(100)
turtle.done()

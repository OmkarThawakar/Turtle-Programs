import turtle
def forward(distance):
    while distance > 0:
        if (turtle.xcor() > 100
            or turtle.xcor() < -100
            or turtle.ycor() > 100
            or turtle.ycor() < -100):
            turtle.setheading(turtle.towards(0,0))
        turtle.forward(1)
        distance = distance - 1

forward(500)
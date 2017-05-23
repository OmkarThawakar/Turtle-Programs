import turtle
def forward(distance):
    while distance > 0:
        if turtle.distance(0,0) > 100:
            angle = turtle.towards(0,0)
            turtle.setheading(angle)
        turtle.forward(1)
        distance = distance - 1
		
forward(200)

import turtle
condition = True
if condition:
    print("condition met")

if not condition:
    print("condition not met")

direction = -30
if direction > 0 :
    turtle.forward(direction)
else:
    turtle.left(180)
    turtle.forward(-direction)
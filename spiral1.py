import turtle 

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(200)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(400)
    painter.left(123)
    
turtle.done()
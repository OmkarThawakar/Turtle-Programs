import turtle 
turtle.speed(5)
spiral = turtle.Turtle()

for i in range(100):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()
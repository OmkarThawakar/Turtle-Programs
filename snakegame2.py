from turtle import *
import random

setup(700, 700)
title("Snake Game!")
bgcolor("pink")

# Boundary
bPen = Pen()
bPen.color("Orange")
bPen.up()
bPen.goto(-300, -300)
bPen.down()

for i in range(4):
    bPen.ht()
    bPen.fd(600)
    bPen.lt(90)



# Player 
playerPen = Pen()
playerPen.color("Orange")
playerPen.up()
playerPen.width(4)

# Create Circle

circle = Pen()
circle.shape("circle")
circle.color("Red")
circle.up()
circle.speed(0)
circle.goto(-100, 100)



# Speed
speed = 1

# Movement functions

def left():
    playerPen.lt(90)

def right():
    playerPen.rt(90)

def speedBoost():
    global speed
    speed += 1


# Key Prompts
onkey(left, "Left")
onkey(right, "Right")
onkey(speedBoost, "Up")
listen()


# Infinity loop and player knockback
while True:
    playerPen.fd(speed)

    if playerPen.xcor() < -300 or playerPen.xcor() > 300:
        playerPen.rt(180)

    elif playerPen.ycor() < - 300 or playerPen.ycor() > 300:
        playerPen.rt(180)

    # Collision with circle
    if playerPen.xcor() == circle.xcor() and playerPen.ycor() == circle.ycor():
        circle.goto(random.randint(-300, 300), random.randint(-300, 300))


done()
import turtle
import random

def walk():
    while turtle.distance(0, 0) < 300:
        turtle.forward(5)
        if random.random() > 0.62:
            turtle.left(10)
        else:
            turtle.right(10)

def pattern(n):
    for _ in range(n):
        turtle.pendown()
        walk()
        turtle.penup()
        turtle.home()

        

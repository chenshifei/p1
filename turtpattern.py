from turtle import *

def square(size):
    for _ in range(4):
        forward(size)
        left(90)

def squares(n):
    for _ in range(n):
        square(20)
        penup()
        forward(30)
        left(24)
        pendown()

def pattern():
    reset()
    speed(10)                   # max speed
    pencolor('green')
    fillcolor('yellow')
    for _ in range(3):
        pendown()
        # 15 squares because there is a turn 24 degrees between each,
        # and 15*24 = 360, a full circle
        squares(15)
        penup()
        forward(80)
        begin_fill()
        circle(30)
        end_fill()
        left(120)
        forward(250)

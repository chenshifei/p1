from turtle import *

def sprial():
    spria(90, 40)

def spria(angle, steps):
    size = 10
    for n in range(steps):
        forward(size)
        left(angle)
        size += 1

def pattern():
    speed(10)
    for i in range(12):
        spria(75, 50)
        forward(100)
    undo()

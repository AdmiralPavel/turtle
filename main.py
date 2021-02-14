import math
import turtle


def dragon(level, length, sign=-1):
    if level == 1:
        turtle.forward(length)
    else:
        turtle.left(45 * sign)
        dragon(level - 1, length / math.sqrt(2), 1)
        turtle.right(90 * sign)
        dragon(level - 1, length / math.sqrt(2), -1)
        turtle.left(45 * sign)


turtle.reset()
turtle.speed(0)
dragon(7, 500)
turtle.done()
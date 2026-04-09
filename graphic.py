from turtle import *
import colorsys

bgcolor('black')
tracer(30)
speed(0)
hideturtle()
pensize(2)

h = 0.9
for i in range(860):
    pencolor(colorsys.hsv_to_rgb(h, 0.9, 1))
    h += 0.004
    penup()
    goto(0, 0)
    pendown()

    forward(170)
    circle(40, 180)
    right(1)
update()
done()
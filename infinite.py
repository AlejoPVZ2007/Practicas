from turtle import *
import colorsys

bgcolor('black')
setup(800, 700)
tracer(40)
speed(0)
width(1)
for i in range(820):
    h = i / 120
    r, g , b = colorsys.hsv_to_rgb(h, 0.9, 1)
    color(r, g, b)
    penup()
    goto(0, 0)
    setheading(i * 3)
    forward(20)
    pendown()
    circle(40 + i/8, 180)
    if i % 20 == 0:
        update()
hideturtle()
update()
done()
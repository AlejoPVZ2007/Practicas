import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.speed(0)
t.width(2)

h=0

for i in range(300):
    color = colorsys.hsv_to_rgb(h,1,1)
    h+=0.01
    t.pencolor(color)

    t.forward(i*2)
    t.right(59)
    t.circle(40, 120)
    t.left(30)

turtle.done()
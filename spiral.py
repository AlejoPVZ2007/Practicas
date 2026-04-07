from turtle import *
tracer(5)
bgcolor('black')
colors = ['white', 'red']

for i in range(200):
    color(colors[i % 2])
    rt(i)
    circle(200,  i + 2)
    fd(i)
    rt(180)
    fd(i)
    hideturtle()
done()
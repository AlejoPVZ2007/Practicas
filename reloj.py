import turtle
import time
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(3)

def draw_clock():
    t.clear()

    t.penup()
    t.goto(0, 0)
    t.setheading(0)

    t.color("white")
    t.penup()
    t.goto(0, -200)
    t.setheading(0)
    t.pendown()
    t.circle(200)

    for i in range(12):
        angle = math.radians(i * 30)
        x = 170 * math.sin(angle)
        y = 170 * math.cos(angle)
        
        t.penup()
        t.goto(x, y)
        t.dot(10)

    t.penup()
    t.goto(0, 0)
    t.setheading(60)
    t.pendown()
    t.forward(80)

    t.penup()
    t.goto(0, 0)
    t.setheading(120)
    t.pendown()
    t.forward(120)

sec_hand = turtle.Turtle()
sec_hand.hideturtle()
sec_hand.speed(0)
sec_hand.color("red")
sec_hand.width(2)

while True:
    draw_clock()

    sec = int(time.strftime("%S"))
    angle = 90 - (sec * 6)

    sec_hand.clear()
    sec_hand.penup()
    sec_hand.goto(0, 0)
    sec_hand.setheading(angle)
    sec_hand.pendown()
    sec_hand.forward(150)

    screen.update()
    time.sleep(1)
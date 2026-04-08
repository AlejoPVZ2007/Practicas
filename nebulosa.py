import turtle 
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

vizualizar_turtles = []
for i in range(180):
    new_t = turtle.Turtle()
    new_t.hideturtle()
    new_t.speed(0)
    new_t.penup()
    vizualizar_turtles.append(new_t)

angle = 0

def draw_core(t, size):
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.color("#1a1a2e")
    t.begin_fill()
    t.circle(size)
    t.end_fill()

    t.penup()
    t.goto(0, -size + 10)
    t.pendown()
    t.color("#16213e")
    t.begin_fill()
    t.circle(size - 10)
    t.end_fill()

    t.penup()
    t.goto(0, -15)
    t.pendown()
    t.color("#0f3460")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

def update_vizualizar():
    global angle

    t.clear()
    draw_core(t, 60)

    for i, visual_t in enumerate(vizualizar_turtles):
        theta = (i * 360 / len(vizualizar_turtles))

        wave1 = math.sin(math.radians(theta * 3 + angle * 2))
        wave2 = math.cos(math.radians(theta * 5 - angle * 3))
        magnitude = 70 + (wave1 * 30) + (wave2 * 20)

        hue = (theta / 360 + angle * 0.002) % 1.0
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

        visual_t.clear()
        visual_t.penup()
        visual_t.goto(0, 0)
        visual_t.setheading(theta)
        visual_t.forward(60)

        visual_t.pendown()
        visual_t.pencolor(rgb)
        visual_t.pensize(2)
        visual_t.forward(magnitude)
        visual_t.dot(3, "white")

    screen.update()
    angle += 6
    screen.ontimer(update_vizualizar, 20)

update_vizualizar()
turtle.done()
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(30)
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

t.width(2)

def tree(branch_len):
    if branch_len > 5:

        if branch_len < 20:
            t.pencolor("lime")
        else:
            t.pencolor("brown")

        t.pensize(branch_len / 10)

        t.forward(branch_len)

        angle = random.randint(15, 30)
        
        t.right(angle)
        tree(branch_len - random.randint(10, 15))

        t.left(angle * 2)
        tree(branch_len - random.randint(10, 15))

        t.right(angle)

        t.backward(branch_len)
    
    else:

        t.dot(random.randint(6, 10), random.choice(["red", "yellow", "orange", "lime", "cyan", "magenta"]))

tree(120)

turtle.done()

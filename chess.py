import turtle

screen = turtle.Screen()
screen.title("Chess Board")
screen.setup(width=600, height=600)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
square_size = 50

start_x = -200
start_y = 200

for row in range(8):
    for col in range(8):
        x = start_x + col * square_size
        y = start_y - row * square_size
        if (row + col) % 2 == 0:
            pen.fillcolor("white")
        else:
            pen.fillcolor("gray")

        pen.penup()
        pen.goto(x, y)
        pen.pendown()

        pen.begin_fill()
        for _ in range(4):
            pen.forward(square_size)
            pen.right(90)
        pen.end_fill()

pen.penup()
pen.goto(start_x, start_y)
pen.pendown()
pen.pensize(3)
pen.color("brown")
for _ in range(4):
    pen.forward(square_size * 8)
    pen.right(90)

screen.mainloop()
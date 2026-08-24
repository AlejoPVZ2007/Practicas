from turtle import *
import math

bgcolor('black')
tracer(20)
speed(0)
hideturtle()
pensize(1)

vertices = []
for i in range(256):
    v =[]
    for j in range(8):
        v.append(1 if (i >> j) & 1 else -1)
    vertices.append(v)

def project(p):
    x = y = 0
    for i in range(8):
        a = 0.3 + i * 0.2
        r = 55 - i * 4
        x += p[i] * math.cos(a) * r
        y += p[i] * math.sin(a) * r
    return (x, y)

edges = []
for i in range(256):
    for j in range(i+1, 256):
        d = 0
        for k in range(8):
            if vertices[i][k] != vertices[j][k]:
                d += 1
        if d == 1:
            edges.append((i, j))

points = [project(v) for v in vertices]

for e in edges:
    x1, y1 = points[e[0]]
    x2, y2 = points[e[1]]
    penup()
    goto(x1, y1)
    pendown()
    pencolor('white')
    goto(x2, y2)

for x, y in points:
    penup()
    goto(x, y)
    dot(6, 'red')

update()
done()
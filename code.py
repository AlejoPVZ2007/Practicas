import math
from turtle import *

tracer(10)
bgcolor('black')

for i in range(4300):
    color("orange")
    t = i/46
    x = 25 * math.cos(5*t) * math.sin(t)
    y = 25 * math.sin(5*t) * math.cos(t)
    goto(x*10, y*10)
    goto(0, 0)
done()
import math
from turtle import *
import colorsys as cs

tracer(10)
bgcolor('black')
h = 0.9

for i in range(2500):
    c = cs.hsv_to_rgb(h, 1, 1)
    t = i/40
    x = 15 * (math.cos(t) + 0.3 * math.cos(15*t))
    y = 15 * (math.sin(t) + 0.3 * math.sin(15*t))
    goto(x*12, y*12)
    color(c)
    h += 0.004
    goto(0, 0)
done()
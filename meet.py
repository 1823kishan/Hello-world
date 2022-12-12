from turtle import*
import colorsys

bgcolor('black')
pensize(2)
speed(0)
h=0.0

for i in range(150):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    pencolor(color)
    h+=0.005
    for j in range(2):
        forward(i)
        right(30)
        forward(50)
        right(120)
        right(121)
        tracer(2)

        hideturtle()
        done()
        
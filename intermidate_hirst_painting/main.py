import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract('61RQCX9SJKL.jpg', 8)
list_colors = []
my_dot = Turtle()
for item in range(len(colors)):
    r = colors[item].rgb.r / 255
    g = colors[item].rgb.g / 255
    b = colors[item].rgb.b / 255
    list_colors.append((r, g, b))

count = 0
for item in range(40):
    if (item+1) % 10 == 0:
        my_dot.penup()
        count += 1
        my_dot.setheading(90)
        my_dot.forward(50)
        if count % 2 == 0:
            my_dot.setheading(360)
        else:
            my_dot.setheading(180)
        my_dot.forward(25)
        my_dot.pendown()
    else:
        my_dot.penup()
        my_dot.dot(20, random.choice(list_colors))
        my_dot.forward(25)
        my_dot.pendown()


screen = Screen()
screen.exitonclick()
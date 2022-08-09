from turtle import Turtle, Screen

steps_start = 10
my_circle = Turtle()
my_circle.speed('fastest')
for _ in range(int(360/5)):
    current_heading = my_circle.heading()
    print(current_heading)
    my_circle.setheading(current_heading + 5)
    my_circle.circle(100)

screen = Screen()
screen.exitonclick()

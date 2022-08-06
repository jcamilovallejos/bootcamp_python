from turtle import Turtle, Screen

start_in_x = 0
steps_in_x = 10
dashed_line_range = 20
dashed_line = Turtle()
for i in range(dashed_line_range):

    if(i+1) == dashed_line_range:
        dashed_line.color("black")
        start_in_x += steps_in_x
        dashed_line.setpos(start_in_x, 0)
    else:
        if ((i+1) % 2) == 0:
            dashed_line.color("white")
            start_in_x += steps_in_x
            dashed_line.setpos(start_in_x, 0)
        else:
            dashed_line.color("black")
            start_in_x += steps_in_x
            dashed_line.setpos(start_in_x, 0)

screen = Screen()
screen.exitonclick()
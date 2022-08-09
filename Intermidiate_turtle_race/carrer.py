from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make yor bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "blue", "purple"]
start_in_y = -150
all_turtles = []

for my_turtle in range(len(colors)):
    start_in_y += 50
    tim = Turtle(shape="turtle")
    tim.color(colors[my_turtle])
    tim.penup()
    tim.goto(-240, start_in_y)
    tim.pendown()
    all_turtles.append(tim)


if user_bet:
    is_race_on = True


while is_race_on:
    for my_turtle in range(len(all_turtles)):
        random_distance = random.randint(0, 10)
        all_turtles[my_turtle].penup()
        all_turtles[my_turtle].forward(random_distance)
        all_turtles[my_turtle].pendown()
        if all_turtles[my_turtle].position()[0] >= 200:
            is_race_on = False
            color_winner_color = all_turtles[my_turtle].pencolor()


if user_bet == color_winner_color:
    print('You are the winner' + color_winner_color)
else:
    print('The winner was ' + color_winner_color)


screen.exitonclick()
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)/255
    g = random.randint(0, 255)/255
    b = random.randint(0, 255)/255
    color = (r, g, b)
    return color


random_walk = Turtle()
range_random_numbers = [i for i in range(100)]
choose_random_number = range_random_numbers
random_range = random.choice(choose_random_number)
walk_block = Turtle()
walk_block.speed("fastest")
walk_block_steps = 20
for _ in range(random_range):
    walk_block.shape("arrow")
    walk_block.color(random_color())
    walk_block.width(15)
    walk_block.forward(walk_block_steps)
    walk_block.right(random.choice([90, -90]))


screen = Screen()
screen.exitonclick()
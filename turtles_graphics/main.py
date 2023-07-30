#class and objects

import turtle as t
import random

timmy = t.Turtle()

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(180)
#         timmy.right(angle)

# for shape_side in range(3,11):
#     draw_shape(shape_side)

t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    color = (r,g,b)
    return color

timmy.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+10)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
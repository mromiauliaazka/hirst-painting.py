# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle
import random

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(193, 167, 121), (220, 213, 116), (145, 84, 60), (169, 162, 50), (144, 176, 157), (146, 71, 88), (138, 170, 185), (188, 145, 158), (55, 123, 89), (44, 110, 139), (53, 24, 13), (131, 28, 43), (17, 29, 49), (69, 16, 28), (178, 96, 113), (14, 48, 33), (169, 206, 186), (184, 102, 86), (224, 172, 183), (227, 174, 167), (214, 213, 20), (68, 151, 170), (90, 151, 105), (18, 93, 58), (128, 34, 27), (159, 206, 214)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
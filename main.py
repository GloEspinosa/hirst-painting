# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# # print(colours)
#
# rgb_colors = []
#
# for color in colors:
#     # r = color.rgb.r
#     # g = color.rgb.g
#     # b = color.rgb.b
#     color_r = color.rgb[0]
#     color_g = color.rgb[1]
#     color_b = color.rgb[2]
#     new_color = (color_r, color_g, color_b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
mushu = turtle_module.Turtle()
mushu.speed(0)

color_list = [(225, 158, 56), (112, 177, 123), (162, 53, 80), (83, 168, 87), (81, 30, 44), (179, 152, 44),
              (134, 99, 57), (149, 29, 55), (206, 134, 164), (44, 135, 86), (115, 162, 184), (6, 63, 108),
              (66, 100, 133), (52, 163, 182), (188, 86, 112), (25, 61, 110), (182, 101, 90), (5, 79, 116),
              (9, 111, 71), (224, 169, 188), (111, 122, 156), (67, 39, 35), (177, 188, 214), (230, 174, 160)]

# Mover la tortuga para que empiece el camino desde abajo a la izquierda
mushu.penup()
mushu.hideturtle()
mushu.setheading(225)
mushu.forward(300)
mushu.setheading(0)
number_of_dots = 100


def draw_dot():
    for dot_count in range(1, number_of_dots + 1):
        mushu.dot(20, random.choice(color_list))
        mushu.forward(50)

        if dot_count % 10 == 0:
            mushu.setheading(90)
            mushu.forward(50)
            mushu.setheading(180)
            mushu.forward(500)
            mushu.setheading(0)


draw_dot()

screen = turtle_module.Screen()
screen.exitonclick()

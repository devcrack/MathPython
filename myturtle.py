from turtle import *
from random import randint

title("Math with Python")
screen = Screen()
screen.colormode(255)


def simple_turtle():
    # Blank shape for not show figures.

    shape('blank')
    # circle_squares()
    # square_trail_by_loop()
    # triangle_figure(300)
    # simple_polygon(100, 5)
    # turtle_spiral()
    # draw_start()
    draw_star_spiral(45)
    exitonclick()


def turtle_ex0():
    forward(100)
    shape('turtle')
    #
    right(45)
    forward(150)


def turtle_do_square_trail():
    shape('turtle')
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)


def square_trail_by_loop():
    for i in range(4):
        forward(200)
        right(90)
        # pencolor(randint(0, 255), randint(0, 255), randint(0, 255))


def circle_squares():
    for i in range(72):
        square_trail_by_loop()
        # for j in range(4):
        #     forward(200)
        #     right(90)
        pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        right(5)


def triangle_figure(side_length):
    for i in range(3):
        forward(side_length)
        right(120)


def simple_polygon(side_lenght, sides_number):
    angle = 360 / sides_number

    for i in range(sides_number):
        forward(side_lenght)
        right(angle)


def turtle_spiral():
    length = 25
    for i in range(60):
        simple_polygon(length, 4)
        right(5)
        length += 5


def draw_start(length):
    for i in range(5):
        forward(length)
        right(144)


def draw_star_spiral(ini_length):
    a_length = ini_length
    for i in range(60):
        draw_start(a_length)
        right(5)
        a_length += 5

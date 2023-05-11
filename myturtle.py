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
    triangle_figure(300)
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
        right(120)
        forward(side_length)





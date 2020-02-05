# Mario DeCristofaro
# md2224
# Lab 9 - Draw Stars

# generates star graphic but needs the file for input still

import turtle
screen = turtle.Screen()
screen.screensize(500, 500)
t = turtle.Turtle()

t.speed(0)
turtle.tracer(0, 0)

screen.bgcolor("black")
t.pencolor("white")
t.fillcolor("white")

file = open("stars.txt", "r")


def read_coords(file):
    first_dict = {}
    second_dict = {}
    third_dict = {}
    for line in file:   # loop
        list = line.split(" ")   # need to split ; and space
        add_first = {list[3]: [list[0], list[1]]}
        add_second = {list[3]: list[4]}
        if len(list) == 7:  # Adds key if one name of star
            add_third = {list[6]: list[3]}
            third_dict.update(add_third)
        elif len(list) > 7:
            for i in range(len(list)):
                name = " ".join(list[6:])
            add_third = {name: list[3]}  # Trying to get multiple keys
            third_dict.update(add_third)
        first_dict.update(add_first)
        second_dict.update(add_second)
    tup = (first_dict, second_dict, third_dict)
    print(tup)
    return tup


def plot_plain_stars(tup):
    for i in tup[0]:
        t.penup()
        x = float(tup[0][i][0])*500/2
        y = float(tup[0][i][1])*500/2
        t.goto(x, y)
        t.pendown()
        t.forward(2)
        t.right(90)
        t.forward(2)
        t.right(90)
        t.forward(2)
        t.right(90)
        t.forward(2)
        t.hideturtle()


def plot_by_magnitude(tup):
    mag_dict = tup[1]
    for i in tup[0]:
        t.begin_fill()
        star_size = round(10.0/(float(mag_dict[i])+2))
        if star_size > 8.0:
            star_size = 8.0
        t.penup()
        x = float(tup[0][i][0])*500/2
        y = float(tup[0][i][1])*500/2
        t.goto(x, y)
        t.pendown()
        t.forward(star_size)
        t.right(90)
        t.forward(star_size)
        t.right(90)
        t.forward(star_size)
        t.right(90)
        t.forward(star_size)
        t.hideturtle()
        t.end_fill()


tup = read_coords(file)
# plot_plain_stars(tup)
plot_by_magnitude(tup)
turtle.update()
turtle.exitonclick()

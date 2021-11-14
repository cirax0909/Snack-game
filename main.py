import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")


segments = []


for n in range(0, 3):
    space = -20
    tim = Turtle()
    tim.color("white")
    tim.shape("square")
    tim.penup()
    tim.goto(x=0+n*space, y=0)
    segments.append(tim)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")

for n in range(0, 3):
    space = -20
    tim = Turtle()
    tim.color("white")
    tim.shape("square")
    tim.penup()
    tim.goto(x=0+n*space, y=0)

screen.exitonclick()

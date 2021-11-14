from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for n in range(0, 3):
            space = -20
            tim = Turtle()
            tim.color("white")
            tim.shape("square")
            tim.penup()
            tim.goto(x=0 + n * space, y=0)
            self.segments.append(tim)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

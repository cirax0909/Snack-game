from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=270)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


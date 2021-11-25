from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        # self.high_score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.clear()
        self.goto(x=-200, y=270)
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 20, 'normal'))
        self.goto(x=0, y=270)
        self.write(f'Highest Score: {self.high_score}', move=False, align='center', font=('Arial', 20, 'normal'))
        with open("score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()



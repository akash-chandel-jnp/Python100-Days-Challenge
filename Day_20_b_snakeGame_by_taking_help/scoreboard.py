from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", False, align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

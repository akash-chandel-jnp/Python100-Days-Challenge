from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", 'r') as file:
            content = file.read()
        self.highscore = int(content)
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score : {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over_msg(self):
    #     self.setposition(0, 0)
    #
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

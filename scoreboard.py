from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write('Hit! Game Over!', align='center', font=(FONT))

    def up_score(self):
        self.score += 1
        self.clear()
        self.goto(-200,250)
        self.write(f'Score = {self.score}', align='center', font=(FONT))

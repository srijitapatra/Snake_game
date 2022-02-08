from turtle import Turtle

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(0,269)
        self.write(f"score:{self.score}", align="center", font=("Courier", 20, "normal"))

    def change(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"score:{self.score}",align = "center",font=("Courier",20,"normal"))

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))

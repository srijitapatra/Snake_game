from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.speed('fastest')
        self.color("red")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-270,270)
        y_cor = random.randint(-270,270)
        self.setposition(x_cor,y_cor)

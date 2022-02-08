from turtle import Turtle
UP = 90
DOWN = 270
LEFT=180
RIGHT =0
POSITION = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.units = []
        self.create()


    def add_segment(self,x):
        tim = Turtle(shape='square')
        tim.color('white')
        tim.penup()
        tim.setposition(x)
        self.units.append(tim)

    def create(self):
        for x in POSITION:
            self.add_segment(x)

    def extend(self):
        self.add_segment(self.units[-1].position())

    def move(self):
        for i in range(len(self.units) - 1, 0, -1):
            new_x = self.units[i - 1].xcor()
            new_y = self.units[i - 1].ycor()
            self.units[i].setposition(new_x, new_y)
        self.units[0].forward(20)

    def up(self):
        if self.units[0].heading() != DOWN:
            self.units[0].setheading(UP)

    def down(self):
        if self.units[0].heading() != UP:
            self.units[0].setheading(DOWN)

    def left(self):
        if self.units[0].heading() != RIGHT:
            self.units[0].setheading(LEFT)

    def right(self):
        if self.units[0].heading() != LEFT:
            self.units[0].setheading(RIGHT)
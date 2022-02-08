from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Score_board
screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

s =Snake()
food= Food()
score = Score_board()

screen.listen()
screen.onkey(s.up,'Up')
screen.onkey(s.down,'Down')
screen.onkey(s.left,'Left')
screen.onkey(s.right,'Right')
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.units[0].distance(food)<15:
        food.refresh()
        s.extend()
        score.change()

    for u in s.units[1:]:

        if s.units[0].distance(u)<10:
            score.game_over()
            game_is_on = False

    if s.units[0].xcor() >290 or s.units[0].xcor() <-290 or s.units[0].ycor() >290 or s.units[0].ycor() <-290 :
        score.game_over()
        game_is_on=False

screen.exitonclick()



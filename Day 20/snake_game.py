from random import randint
from time import sleep
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.go_up,"Up")
screen.onkey(snake.go_down,"Down")
screen.onkey(snake.go_left,"Left")
screen.onkey(snake.go_right,"Right")

game_on = True
while game_on:
    screen.update()
    snake.move_snake()        

screen.exitonclick()
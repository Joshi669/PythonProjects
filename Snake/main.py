from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increaseScore()

    #Detect Collision with Wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.gameover()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()

screen.exitonclick()
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=700, width=700)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # detection of snake's collision with the food
    if snake.head.distance(food.x_cord, food.y_cord) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_length()

    # detection of snake's collision with walls
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        scoreboard.score_reset()
        snake.reset_snake()

    # detect snake's collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment.position()) < 10:
            scoreboard.score_reset()
            snake.reset_snake()

    snake.move()

screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

game_is_on = True
cnt = 0

while game_is_on:
    time.sleep(0.1)
    if cnt == 5:
        cars.add_car()
        cnt = 0
    cnt += 1
    cars.cars_move()

    if cars.detect_collision(player):
        score.game_over()
        game_is_on = False

    if player.ycor() == 280:
        player.next_level()
        cars.next_level()
        score.next_level()

    screen.update()

screen.exitonclick()

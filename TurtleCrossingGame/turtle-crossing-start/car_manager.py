from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarInitial(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x_cor, random.randint(-250, 250))


class CarManager:

    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        for _ in range(20):
            new_car = CarInitial(random.randint(-280, 280))
            self.cars.append(new_car)

    def cars_move(self):
        for car in self.cars:
            new_x = car.xcor() - self.cars_speed
            car.goto(new_x, car.ycor())

    def next_level(self):
        self.cars_speed += MOVE_INCREMENT

    def add_car(self):
        new_car = CarInitial(280)
        self.cars.append(new_car)

    def detect_collision(self, player):
        for car in self.cars:
            if abs(car.ycor() - player.ycor()) < 20 and abs(car.xcor() - player.xcor()) < 28:
                return True
        return False

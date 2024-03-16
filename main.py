from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# creating and setting up the screen
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING")

# get the player class with the object
player = Player()
carmanager = CarManager()
score = Scoreboard()

# listen for the key movement
screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()  # for the animation

    carmanager.create_car()
    carmanager.move_cars()

    # detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()

    # detect successful collision
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        score.increase_level()

screen.exitonclick()

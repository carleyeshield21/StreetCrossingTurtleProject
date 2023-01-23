import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, 'w')
screen.onkey(player.move_back, 's')

time_speed = 0.1
# time_increment = 0.009
time_increment = 0.01
game_is_on = True
while game_is_on:
    car.create_car()
    car.car_forward()
    # car.car_start()
    time.sleep(time_speed)
    # time.sleep(0.05)
    screen.update()

    if player.ycor() >= 290:
        player.reset_position()
        time_speed -= time_increment
        if time_speed == 1.0408340855860843e-17:
            time_increment = 0
            time_speed = 0
        print(time_speed)
        score.up_score()

    if player.ycor() <= -295:
        player.goto(0, -280)

    for car1 in car.all_cars:
        # print(car1)
        if car1.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
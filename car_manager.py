from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        # self.time_speed = 0.1

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 260)
            new_car.goto(265, random_y)
            self.all_cars.append(new_car)

    def car_forward(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    # def car_start(self):
    #     # time_speed = 0.1
    #     time.sleep(time_speed)



    # def __init__(self):
    #     super().__init__()
    #     self.all_cars = []
    #     self.shape('square')
    #     self.penup()
    #     self.color(random.choice(COLORS))
    #     self.shapesize(stretch_wid=1, stretch_len=2)
    #     self.random_y = random.randint(-250, 260)
    #     self.goto(265, self.random_y)
    #     # self.goto(265,-250)
    #     # -250, 260
    #     # pass
    #
    # def car_forward(self):
    #     self.back(STARTING_MOVE_DISTANCE)

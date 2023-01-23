from  turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
    # pass

    def move_forward(self):
        # new_ycor = self.ycor() + MOVE_DISTANCE
        # self.goto(0, new_ycor)
        # shorter code below
        self.forward(MOVE_DISTANCE)

    def move_back(self):
        # new_ycor = self.ycor() - MOVE_DISTANCE
        # self.goto(0, new_ycor)
        # shorter code below
        self.forward(MOVE_DISTANCE*(-1))

    def reset_position(self):
        self.goto(STARTING_POSITION)
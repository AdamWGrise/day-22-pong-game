from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.goto(position)
        self.color("white")
        self.penup()
        self.v_distance = 10
        self.h_distance = 10

    def move_up(self, distance):
        return self.ycor() + distance

    def move_down(self, distance):
        return self.ycor() - distance

    def move(self):
        new_x = self.xcor() + self.h_distance
        new_y = self.ycor() + self.v_distance
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.v_distance *= -1

    def paddle_bounce(self):
        self.h_distance *= -1
        # if self.h_distance < 0:
        #     self.h_distance -= 0.05 * random.randint(3, 10)
        # else:
        #     self.h_distance += 0.05 * random.randint(3, 10)

    def point_score(self, side):
        print("Point for " + side + " player")
        self.goto(0, 0)
        self.h_distance *= -1

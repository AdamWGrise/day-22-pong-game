from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.goto(position)
        self.color("white")
        self.penup()
        self.base_distance = 3
        self.v_distance = self.base_distance
        self.h_distance = self.base_distance

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
        prev_h_speed = self.h_distance
        self.h_distance = self.h_distance + self.h_distance * random.uniform(-0.2, 0.2)
        h_speed_change = self.h_distance - prev_h_speed
        if self.v_distance > 0:
            self.v_distance = self.v_distance + h_speed_change
        else:
            self.v_distance = self.v_distance - h_speed_change
        if self.h_distance < 0:
            self.h_distance -= 0.05 * random.randint(3, 10)
        else:
            self.h_distance += 0.05 * random.randint(3, 10)

    def reset_speed(self):
        if self.h_distance > 0:
            self.h_distance = self.base_distance
        else:
            self.h_distance = self.base_distance * -1
        if self.v_distance > 0:
            self.v_distance = self.base_distance
        else:
            self.v_distance = self.base_distance * -1

    def point_score(self, side):
        print("Point for " + side + " player")
        self.goto(0, 0)
        self.reset_speed()
        self.h_distance *= -1

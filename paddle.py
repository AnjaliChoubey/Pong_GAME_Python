from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, current_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(current_pos)

    def move_up(self):
        y_cor = self.ycor() + 20
        x_cor = self.xcor()
        self.goto(x_cor, y_cor)


    def move_down(self):
        y_cor = self.ycor() - 20
        x_cor = self.xcor()
        self.goto(x_cor, y_cor)

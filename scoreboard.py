from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", move=False, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.r_score}", move=False, align='center', font=('Courier', 50, 'normal'))

    def check_l_score(self):
        self.l_score +=1
        self.update_score()

    def check_r_score(self):
        self.r_score +=1
        self.update_score()
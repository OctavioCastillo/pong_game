from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(0, 200)
        self.write(":", align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def add_r_point(self):
        self.r_score += 1
        self.update()

    def add_l_point(self):
        self.l_score += 1
        self.update()

    def game_over(self):
        self.clear()
        self.goto(-150, 0)
        self.write(self.l_score, align="center", font=("Courier", 120, "normal"))
        self.goto(0, 0)
        self.write(":", align="center", font=("Courier", 120, "normal"))
        self.goto(150, 0)
        self.write(self.r_score, align="center", font=("Courier", 120, "normal"))
        self.goto(0, -100)
        if self.l_score > self.r_score:
            self.write("<=== WINS", align="center", font=("Courier", 80, "normal"))
        else:
            self.write("WINS ===>", align="center", font=("Courier", 80, "normal"))


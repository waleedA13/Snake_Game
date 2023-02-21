from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.up()
        self.pencolor("white")
        self.setposition(0, 300)
        self.write(f"Score: {self.score} ", False, "center",
                   ("Arial", 15, "normal"))

    def update_scoreboard(self):
        """Updates the score after every food is eaten"""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score} ", False, "center", ("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     """Shows the (Game Over)"""
    #     self.setposition(0, 0)
    #     self.color("purple")
    #     self.write("Game Over", False, "center", ("Arial", 20, "normal"))
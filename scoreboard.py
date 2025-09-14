from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 370)
        self.score = 0 
        self.high_score = self.get_from_file()
        self.print_score()

    def get_from_file(self):
        with open("Score.txt") as file:
            return int(file.read())
    
    def update_file(self):
        with open("Score.txt", "w") as file:
            file.write(str(self.score))

    def print_score(self):
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))    
    
    def increasing_score(self):
        self.score += 1
        self.clear()
        self.print_score()
    
    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0, 0)

        if self.score > self.high_score:
            self.high_score = self.score
            self.update_file()
       
            

        self.write(f"--------GAME OVER--------\n\nFinal score: {self.score} \nHigh Score: {self.high_score}", align="center", font=("arial", 20, "normal"))

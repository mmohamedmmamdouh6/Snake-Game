# make the snake
from turtle import Turtle

class Snake():
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[-1]

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("green")
            new_turtle.penup()
            new_turtle.goto(20*i, 0)
            self.turtles.append(new_turtle)
    
    def move(self):
        for i in range ( len(self.turtles)):
            if (i+1<len(self.turtles)):
                self.turtles[i].goto( self.turtles[i+1].pos() ) # every part follow the previous one 
        self.head.forward(20)
    
    def greater_snake(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("green")
        new_turtle.penup()
        new_turtle.goto(self.turtles[0].pos())
        self.turtles.insert(0, new_turtle)

    def up(self):
        self.head.setheading(90)
    
    def down(self):
        self.head.setheading(90*3)
    
    def left(self):
        self.head.setheading(90*2)
    
    def right(self):
        self.head.setheading(90*4)
    
    
     
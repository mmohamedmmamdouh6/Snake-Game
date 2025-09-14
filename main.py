# This is the game
from turtle import Screen
from shape import Snake
from food import Apple
from scoreboard import Scoreboard
import time

# Setup the window
interFace = Screen()
interFace.setup(850, 850)
interFace.title("SNAKE GAME")
interFace.bgcolor("black")

interFace.tracer(0)

# Call the snake
snake = Snake()
food = Apple()
score = Scoreboard()
interFace.update()

# Start the game
game = True
while game:
    snake.move()
    interFace.update()
    time.sleep(0.1)
    
    # Controle on keyboard
    interFace.listen()

    interFace.onkey(snake.up, "Up")
    interFace.onkey(snake.down, "Down")
    interFace.onkey(snake.left, "Left")
    interFace.onkey(snake.right, "Right")

    # Found the apple
    if snake.head.distance(food) < 15:
        # put a new apple
        food.move() 
        # big up snake
        snake.greater_snake()
        # Increament Score
        score.increasing_score()
    
    # when snake crash with wall
    if snake.head.xcor() >=405 or snake.head.xcor() <=-405 or snake.head.ycor() >= 405 or snake.head.ycor() <=-405:
        score.game_over()
        game = False
        
    # once the snake eat itself
    for part in snake.turtles[0: -1]: # except the head
        if snake.head.distance(part) < 10 : 
            score.game_over()            
            game = False
            break

interFace.exitonclick()
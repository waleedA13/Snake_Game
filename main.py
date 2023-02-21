from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
screen.listen()
speed = .1

# Creates a border
t = Turtle()
t.up()
t.goto(-290, -290)
t.down()
t.color("white")
t.hideturtle()
for loop in range(4):
    t.forward(580)
    t.left(90)

food = Food()
snake = Snake()
screen.update()

# For arrow keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()
game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    snake.move_snake()

    # Checks if snake is going towards a food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_point()
        speed = snake.new_body(speed)

    # Checks if snake is going towards the edge
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor(
    ) > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Checks if snake is going to hit its own body
    for body_part in snake.body[1:]:
        if snake.head.distance(body_part) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

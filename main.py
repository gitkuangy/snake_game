import time
from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 800

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("A Simple Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check the collision with the food
    if snake.head.distance(food) < 20 * 0.8 + 5:
        food.relocation()
        score_board.update_score()
        snake.extend_snake()

    # Check the collision with the wall
    if -WIDTH / 2 < snake.head.xcor() < WIDTH / 2 and -HEIGHT / 2 < snake.head.ycor() < HEIGHT / 2:
        game_is_on = True
    else:
        game_is_on = False
        score_board.game_over()

    # Check the collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()

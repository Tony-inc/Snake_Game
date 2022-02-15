import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
score = Score()

game_is_on = True

while game_is_on:
    time.sleep(0.15)
    snake.move_snake()
    screen.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.squares[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()














screen.exitonclick()
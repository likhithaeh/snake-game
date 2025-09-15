from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("🐍 SNAKE GAME 🐍")
game_on = True
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 20:
        #score.clear()
        food.move_food()
        snake.extend()
        score.score_increase()



    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        #game_on = False
        score.reset()
        snake.reset()

    #Detect collision with tail
    #if head collides with any segment of body :
        #trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
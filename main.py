import time

from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background color
screen.title("My Snake Game")  # title of the window that shows up

screen.tracer(0)

# moving mechanism : Assume 3 segments
#  3rd segment goes to where 2nd used to be and 2nd goes where 1st used to be.
# i.e, nth segment goes to where n-1 used to be and n-1 goes to where n-2 used to be and so on.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # start listening for keystrokes

screen.onkey(snake.up, "Up")  # Case Sensitive
screen.onkey(snake.down, "Down")  # Binding function is the function in the snake object
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # while the game is on, the screen is going to update every 0.1 seconds.

    snake.move()

    # Detect collision with food. (by using the method from turtle class called turtle.distance() ---> this works by
    # comparing the distance from the turtle object to what you put inside the parentheses)

    if snake.head.distance(food) < 15:
        # if distance from the first segment of the snake (head of snake) to the food is less than 15 pixels (food
        # ---> 10 by 10) pretty certain that they collided

        scoreboard.increase_score()
        food.refresh()  # food object goes to a new random location
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:  # slicing avoids the segment of snake's head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

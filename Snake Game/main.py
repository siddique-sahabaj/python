from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# creating and initializing the game screen
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("My Snake Game")


# Making the screen blank
game_screen.tracer(0)

# Taking input from the user about the shape of the snake's segment

available_shapes = game_screen.getshapes()[2:]
segment_shape = game_screen.textinput("Shape", "Enter the shape of the snake segment\n\n"
                                               f"Available Shapes = {available_shapes}\n").lower()

snake = Snake(segment_shape)
food = Food()
score_board = ScoreBoard()

game_screen.listen()# Making the screen listen to the game events


# Adding the event listeners corresponding to the keystrokes
game_screen.onkey(key="Up", fun=snake.move_up)
game_screen.onkey(key="Down", fun=snake.move_down)
game_screen.onkey(key="Left", fun=snake.move_left)
game_screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True # It Decides whether the game should continue or not


while game_is_on:
        game_screen.update()
        time.sleep(snake.speed)
        snake.move()

        # Checking if snake has eaten/collided the food
        if snake.head.distance(food) <= 15:
            score_board.score += 1
            score_board.display_score() # update the score in scoreboard
            food.set_random_position()
            snake.add_segment(snake.segments[-1].position())

            # Increasing the speed of the snake when score is increased by 10 points
            if score_board.score % 10 == 0:
                snake.speed -= 0.01

        if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
            score_board.game_over()
            snake.game_reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) <= 15:
                score_board.game_over()
                snake.game_reset()


game_screen.exitonclick()
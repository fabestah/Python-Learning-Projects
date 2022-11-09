from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


def screen_setup():
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("black")
    s.tracer(0)
    s.title("🐍 Snake Game 🐍")
    return s


if __name__ == "__main__":
    screen = screen_setup()
    snake = Snake()
    food = Food()
    score = Score()
    snake.create_snake()

    game_is_on = True

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Food collision
        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh_food()
            score.update_score()

        # Wall collision
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_is_on = False
            score.game_over()

        # Snake collision
        for seg in snake.segs[1:]:
            if snake.head.distance(seg) == 0:
                game_is_on = False
                score.game_over()

    screen.exitonclick()

# TODO: 1. Player piece (key movement)
# TODO: 2. Game piece (movement)
# TODO: 4. Board (Bounce)
# TODO: 5. Ball
# TODO: 4. Board
# TODO: 5. Scoreboard

from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

game_is_on = True

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=l_paddle.move_up, key='w')
screen.onkey(fun=l_paddle.move_down, key='s')
screen.onkey(fun=r_paddle.move_up, key='Up')
screen.onkey(fun=r_paddle.move_down, key='Down')


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        score.add_l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        score.add_r_point()

    if score.l_score == 5 or score.r_score == 5:
        game_is_on = False
        score.game_over()
        ball.hideturtle()


screen.exitonclick()

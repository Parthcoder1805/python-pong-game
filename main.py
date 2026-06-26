from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from middle_line import MiddleLine


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
middle_line = MiddleLine()


screen.listen()
screen.onkey(key = "Up", fun = r_paddle.go_up)
screen.onkey(key = "Down", fun = r_paddle.go_down)
screen.onkey(key = "w", fun = l_paddle.go_up)
screen.onkey(key = "s", fun = l_paddle.go_down)



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    middle_line.draw_line()


    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
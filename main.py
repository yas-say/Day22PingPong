from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

lcordinate = (-350, 0)
rcordinate = (350, 0)
lpaddle = Paddle(lcordinate)
rpaddle = Paddle(rcordinate)

screen.listen()

screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

flag = True
while flag:
    screen.update()
screen.exitonclick()

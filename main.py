from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

x_coor = 0
y_coor = 0
snake_size = 3

for _ in range(snake_size):
    turtle = Turtle()
    turtle.color("white")
    turtle.shape("square")
    turtle.goto(x=x_coor, y=y_coor)
    x_coor -= 20

screen.exitonclick()

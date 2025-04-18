from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(90)

def clockwise():
    tim.right(90)

def clear_drawing():
    tim.clear()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(counter_clockwise,"a")
screen.onkey(move_backwards,"s")
screen.onkey(clockwise,"d")
screen.onkey(clear_drawing,"c")
screen.exitonclick()
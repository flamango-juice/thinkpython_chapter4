import turtle

def jump(t: turtle.Turtle, length):
    """Moves param:turtle forward by amount param:length.

    turtle: turtle object from turtle module.
    length: length of units the turtle should jump.
    """
    t.penup()
    t.forward(length)
    t.pendown()

def rectangle(t: turtle.Turtle, l,w):
    for length in (l,w,l,w):
        t.forward(length)
        t.left(90)
def setup(t: turtle.Turtle, screen: turtle.Screen,color="black",width=1920,height=1080,speed=1,turtle_color="white"):
    t.speed(speed)
    screen.bgcolor(color)
    screen.setup(width,height)
    t.color(turtle_color)


t = turtle.Turtle()
screen = turtle.Screen()

setup(t,screen)
#exercise 1
rectangle(t,80,40)

turtle.exitonclick()


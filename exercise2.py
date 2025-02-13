
import turtle


def rhombus(t: turtle.Turtle, length, angle):
    angle_dos = 180 - angle
    for g in range(2):
        t.forward(length)
        t.right(angle)
        t.forward(length)
        t.right(angle_dos)

def setup(t: turtle.Turtle, screen: turtle.Screen,color="black",width=1920,height=1080,speed=1,turtle_color="white"):
    t.speed(speed)
    screen.bgcolor(color)
    screen.setup(width,height)
    t.color(turtle_color)

t = turtle.Turtle()
screen = turtle.Screen()
setup(t, screen)

rhombus(t, 50, 60)

turtle.exitonclick()

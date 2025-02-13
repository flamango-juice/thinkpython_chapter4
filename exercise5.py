import turtle
import math

def polyline(t:turtle.Turtle,n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t:turtle.Turtle,radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(t,n, length, step_angle)

def petal(t:turtle.Turtle,radius,angle):
    if angle > 150 or angle <= 0:
        angle = 150
    arc(t,radius,angle)
    t.left(180-angle)
    arc(t, radius, angle)

def flower(t:turtle.Turtle,radius,angle):
    start_angle = t.heading()
    count = 0
    while count == 0 or start_angle != t.heading():
        petal(t,radius,angle)
        count += 1
    print(f"This took {count} petals.")

def setup(t: turtle.Turtle, screen: turtle.Screen,color="black",width=1920,height=1080,speed=1,turtle_color="white"):
    t.speed(speed)
    screen.bgcolor(color)
    screen.setup(width,height)
    t.color(turtle_color)


t = turtle.Turtle()
screen = turtle.Screen()
setup(t, screen,"black", 1920,1080)

flower(t,100,30)

turtle.exitonclick()


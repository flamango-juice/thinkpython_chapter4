import turtle
import math

def triangle(t: turtle.Turtle, leg,base):
    #ta = 180 - 2 * ba
    #ba = (ta - 180) / 2
    a = math.degrees(math.asin(0.5 * base / leg))
    t_a = a * 2
    b_a = (180 - t_a)/2
    t.left(a)
    t.forward(leg)
    t.left(180-b_a)
    t.forward(base)
    t.left(180-b_a)
    t.forward(leg)
    hh = (180 - t_a) - a
    print(t.heading(),hh)
    t.left(hh + t_a)
def draw_pie(t:turtle.Turtle,n,leg):
    base = leg * 2 * math.sin(math.radians(180/n))
    for side in range(n):
      triangle(t,leg,base)



def setup(t: turtle.Turtle, screen: turtle.Screen,color="black",width=1920,height=1080,speed=1,turtle_color="white"):
    t.speed(speed)
    screen.bgcolor(color)
    screen.setup(width,height)
    t.color(turtle_color)


t = turtle.Turtle()
screen = turtle.Screen()
setup(t, screen,"black", 1920,1080,0)

draw_pie(t,3,250)

turtle.exitonclick()
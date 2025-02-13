import  turtle

def parallelogram(t: turtle.Turtle,base,leg,angle):
    comp_angle = 180 - angle
    for _ in range(2):
        t.forward(base)
        t.left(angle)
        t.forward(leg)
        t.left(comp_angle)

def rectangle(t: turtle.Turtle, base,height):
    parallelogram(t, base,height,90)

def rhombus(t,side,angle):
    parallelogram(t,side,side,angle)
def square(t,side):
    parallelogram(t,side,side,90)

def setup(t: turtle.Turtle, screen: turtle.Screen,color="black",width=1920,height=1080,speed=1,turtle_color="white"):
    t.speed(speed)
    screen.bgcolor(color)
    screen.setup(width,height)
    t.color(turtle_color)

t = turtle.Turtle()
screen = turtle.Screen()
setup(t, screen,"black", 1920,1080,0)

parallelogram(t, 50, 74, 89.9)
t.goto(70,100)
rectangle(t,50,100)
t.goto(-150,0)
rhombus(t,90,88)
square(t,90)

for i in range(400):
    rectangle(t, i * 2, i // 2)
    print(i * 2, i // 2)

turtle.exitonclick()
import turtle
col=['green','red','purple','yellow','white','blue']
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(120):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)
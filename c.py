import turtle
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("black screen")

pen=turtle.Turtle()
pen.speed("fastest")
colors = ["red","orange","yellow","green","blue","violet","pink"]
i = 0
while True :
    i = i+1
    pen.color(colors[i % 7])
    pen.circle(100)
    pen.right(5)
    pen.forward(2)

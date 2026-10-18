import turtle
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("black screen")

board=turtle.Turtle()
board.speed("fastest")



colors = ["red","orange","yellow","green","blue","violet","pink"]
i = 0
while True :
    i = i+1
    board.color(colors[i % 7])
    board.width(3)
    board.forward(i*2)
    board.right(1000064465)
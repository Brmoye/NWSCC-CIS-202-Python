#This is a simple Turtle demo

from turtle import Turtle

def square(t, length):
    #Draws a square
    for count in range(4):
        t.forward(length)
        t.left(90)

def rSquare(t, length):
    #Draws a square
    for count in range(4):
        t.forward(length)
        t.right(90)

def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t,length)
        t.left(360 / n)

def hexagon(t, length):
    #Draws a hexagon
    for count in range(6):
        t.forward(length)
        t.left(60)

def main():
    t = Turtle()
    t.screen.bgcolor("purple")
    t.pencolor("white")
    radialHexagons(t, 40, 20)

    #square(t, 200)
    #rSquare(t, 200)

    #square(t, -200)
    #rSquare(t, -200)

    #hexagon(t, -50)
    
#Entry point for program execution
if __name__ == "__main__":
    main()

    

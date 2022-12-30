#Display random patterns of squares with a random fill color

from turtle import Turtle
from polygons import *
import random

def drawPattern(t, x, y, count, length, shape):
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    t.fillcolor((random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255)))
    radialPattern(t, count, length, shape)
    t.end_fill()

def main():
    myTurtle = Turtle()
    myTurtle.speed(0)
    myTurtle.screen.colormode(255)
    
    count = 10 #Number of shapes in pattern

    #Set screen dimensions
    width = myTurtle.screen.window_width() // 2
    height = myTurtle.screen.window_height() // 2
    
    length = 70 #Size of object
    inset = length * 2 #Distance from window boundary

    #Draw squares in upper left corner
    drawPattern(myTurtle, -width + inset, height - inset, count, length, square)

    #Draw squares in lower left corner
    drawPattern(myTurtle, -width + inset, inset - height, count, length, square)

    #Change drawing attributes and draw more shapes
    length = 50 #Size of object
    inset = length * 3 #Distance from window boundary

    #Draw hexagons in lower right corner
    drawPattern(myTurtle, width - inset, inset - height, count, length, hexagon)

    #Draw hexagons in upper right corner
    drawPattern(myTurtle, width - inset, height - inset, count, length, hexagon)

    myTurtle.up()
    myTurtle.goto(0, 0)

#Entry point for program execution
if __name__ == "__main__":
    main()


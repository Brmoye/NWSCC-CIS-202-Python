def square(t, length):
    #Draws a square
    for count in range(4):
        t.forward(length)
        t.left(90)

def radialHexagons(t, n, length):
    for count in range(n):
        hexagon(t,length)
        t.left(360 / n)

def radialPattern(t, n, length, shape):
    for count in range(n):
        shape(t, length)
        t.left(360 / n)

def hexagon(t, length):
    #Draws a hexagon
    for count in range(6):
        t.forward(length)
        t.left(60)



    

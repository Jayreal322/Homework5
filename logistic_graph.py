from graphics import *

def logistic(k, x):
    return k * x * (1 - x)

def main():
    win = GraphWin("Logistic Function Graph", 600, 400)
    win.setCoords(0, 0, 100, 1)

    k = float(input("Enter k value: "))
    x = float(input("Enter starting x value: "))
    n = int(input("Enter number of points: "))

    for i in range(n):
        x = logistic(k, x)

        point = Circle(Point(i, x), 0.4)
        point.setFill("blue")
        point.draw(win)

        print(x)

    win.getMouse()
    win.close()

main()

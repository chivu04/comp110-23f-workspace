from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

i: int = 0
while i < 4:
    leo.forward(300)
    leo.left(90)
    i += 1

leo.penup()
leo.goto(45, 60)
leo.pendown()
 
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1


"""EX05: Sunny Morning Outdoor."""
 
__author__ = "730597416"
 
from turtle import Turtle, colormode, done 

# Set the background color to light blue for the sky
screen = Turtle()
screen.getscreen().bgcolor("lightblue")


def sun(one_turtle: Turtle, x: float, y: float, color: str) -> None:
    """Drawing the sun."""
    one_turtle.penup()
    one_turtle.goto(x, y)
    one_turtle.pendown()
    one_turtle.color("yellow") 
    one_turtle.begin_fill()
    
    sides = 12
    angle = 30
    index = 0
    
    while index < sides:
        one_turtle.forward(30)
        one_turtle.right(angle)
        index += 1

    one_turtle.end_fill()
    one_turtle.penup()


def cloud(two_turtle: Turtle, x: float, y: float, color: str) -> None:
    """Drawing the clouds."""
    two_turtle.penup()
    two_turtle.goto(x, y)
    two_turtle.pendown()
    two_turtle.color("white") 
    two_turtle.setheading(90)
    two_turtle.begin_fill()

    sides = 3
    angle = 180
    index = 0

    while index < sides:
        two_turtle.circle(30, angle)
        two_turtle.right(180)
        index += 1
    
    two_turtle.end_fill()
    two_turtle.penup()


def field(three_turtle: Turtle, x: float, y: float, color: str) -> None:
    """Drawing the field."""
    three_turtle.penup()
    three_turtle.goto(-400, -300)
    three_turtle.pendown()
    three_turtle.color("green")
    three_turtle.begin_fill()

    three_turtle.goto(400, -300)
    three_turtle.goto(400, -200)
    three_turtle.goto(-400, -200)
    three_turtle.goto(-400, -300)

    three_turtle.end_fill()


def main() -> None:
    """The entry point of my scene."""
    colormode(255)
    turtle = Turtle()
    turtle.speed(3)
    
    # Draw the sun
    sun(turtle, 200, 200, "yellow")
    
    # Draw two clouds
    cloud(turtle, 50, 150, "white")
    cloud(turtle, -100, 50, "white")

    # Draw green field
    field(turtle, -400, -300, "green")
    
    done()

if __name__ == "__main__":
    main()
import turtle

def draw_half_filled_circle(radius, fill_color="blue", pen_color="black"):
    """
    Draws a half-filled circle with a specified radius and color.

    Args:
        radius (int): The radius of the circle.
        fill_color (str): The color to fill one half of the circle.
        pen_color (str): The color of the pen lines.
    """
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("Half-Filled Circle")
    screen.bgcolor("white")
    
    # Set up the turtle pen
    pen = turtle.Turtle()
    pen.speed(3)
    pen.color(pen_color)
    pen.pensize(2)

    # Move to the starting position for the first semicircle
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.setheading(90)

    # Begin filling the first half
    pen.fillcolor(fill_color)
    pen.begin_fill()
    
    # Draw the first semicircle
    pen.circle(radius, 180)
    
    # Draw the diameter to close the shape
    pen.setheading(270)
    pen.forward(2 * radius)
    
    # End the fill
    pen.end_fill()

    # Move back to the starting point for the second semicircle
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.setheading(90)
    
    # Draw the second semicircle without filling
    pen.circle(radius, 180)

    # Hide the turtle and keep the window open
    pen.hideturtle()
    screen.mainloop()

# Call the function to draw a half-filled circle with a radius of 100
draw_half_filled_circle(100)

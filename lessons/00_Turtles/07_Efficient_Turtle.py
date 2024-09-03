
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

george = turtle.Turtle()                  # Create a turtle named tina

george.shape('turtle')                    # Set the shape of the turtle to a turtle
george.speed(2)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides 
    side_length =50      # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        george.forward(side_length)
        george.left(angle)   
                                # Move tina forward by the forward distance
        ...                              # Turn tina left by the left turn

george.penup()
george.goto(40,0)
george.pendown()

draw_polygon(4)                        # Draw a square

george.penup()
george.goto(-50,0)
george.pendown()
                                      # Move tina to another spot on the screen

draw_polygon(5)                        # Draw a pentagon

george.penup()
george.goto(-150,0)
george.pendown()                                      # Move tina to another spot on the screen

draw_polygon(6)                        # Draw a hexagon

george.penup()
george.goto(-500,0)
george.pendown() 

turtle.exitonclick()                     # Close the window when we click on it

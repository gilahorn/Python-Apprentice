"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=400, height=500)    # Set the size of the window

tina = turtle.Turtle()
tina.begin_fill()
tina.color('purple')                  # Create a turtle named tina
tina.forward(100)
tina.left(120)
tina.forward(100)
tina.left(120)
tina.forward(100)
tina.end_fill()
tina.left(120)
tina.forward(30)
tina.pencolor('white')
tina.write("miel feig")
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it

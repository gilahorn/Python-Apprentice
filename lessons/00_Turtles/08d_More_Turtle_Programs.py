# Click on the Screen
import turtle as turtle
import random
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")

# This is the function that gets called when you click on the screen
def screen_clicked(x, y):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

   
  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open

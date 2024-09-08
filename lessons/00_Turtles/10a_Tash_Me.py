""" Tash
Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

... # Your code here
import turtle
from pathlib import Path
from PIL import Image

def set_background_image(window, image_name):
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    window.setup(image.width, image.height)
    window.bgpic(image_path)

def set_turtle_image(turtle, image_name):
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen = turtle.Screen()
screen.setup(width=800, height=600)

tina = turtle.Turtle()

set_background_image(screen, "emoji2.png")
set_turtle_image(tina, "moustache2.gif")

tina.speed(3)

tina.penup() 
tina.goto(0, -100) 
tina.pendown() 


turtle.exitonclick()


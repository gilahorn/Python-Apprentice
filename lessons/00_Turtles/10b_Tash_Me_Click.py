# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here )to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
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
 
def move_moustache(x, y):
    tina.penup()  
    tina.goto(x, y) 
    tina.pendown()  


screen = turtle.Screen()
screen.setup(width=800, height=600)

tina = turtle.Turtle()

set_background_image(screen, "emoji2.png")
set_turtle_image(tina, "moustache2.gif")

tina.speed(3)

tina.penup() 
tina.goto(0, -100) 
tina.pendown() 
screen.onclick(move_moustache)

turtle.done()

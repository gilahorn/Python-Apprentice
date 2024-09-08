
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here
import turtle
from pathlib import Path
from PIL import Image

def set_background_image(window, image_name):
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    window.setup(width=image.width, height=image.height)
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

def twirl_moustache(x, y):
    move_moustache(x, y)
    tina.penup()
    for _ in range(50):  
        tina.right(10)  
        tina.forward(5)  
    tina.pendown()

screen = turtle.Screen()
screen.setup(width=800, height=600)

set_background_image(screen, "emoji2.png")
tina = turtle.Turtle()
set_turtle_image(tina, "moustache2.gif")

tina.speed(10)


tina.onclick(twirl_moustache)

turtle.done()


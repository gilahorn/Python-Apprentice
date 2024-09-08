""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""
from pathlib import Path
import turtle as turtle


def set_turtle_image(turtle, image_name):

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()

...  # Your Code Here
screen.addshape('leaguebot_bolt.gif')
t.shape('leaguebot_bolt.gif')
t.shapesize(stretch_wid=10, stretch_len=10)
t.pencolor('blue')

for _ in range(6):
    t.forward(100)
    t.right(60)


turtle.exitonclick()

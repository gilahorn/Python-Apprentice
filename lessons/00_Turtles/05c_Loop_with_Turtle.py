
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
import turtle
turtle.begin_fill()   
turtle.color('purple')
for i in range(5):
    print('Loop Iteration', i)
    turtle.forward(100)
    turtle.left(72)
turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()
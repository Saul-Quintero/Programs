# import tkinter as tk

import turtle


window = turtle.Screen()
window.title('My Turtle')
window.bgcolor('grey')
# window.screensize(1200, 800, bg='blue')


blade = turtle.Turtle()
blade.shape('turtle')
blade.speed(100)
blade.hideturtle()
blade.left(90)
blade.pencolor('darkblue')
for i in range(10):
    blade.clone()
    blade.left(90)
    blade.forward(100)
    blade.


# steve = turtle.Turtle()
# steve.shape('turtle')
# steve.speed(100)
# steve.hideturtle()
# steve.penup()
# steve.left(180)
# steve.forward(75)
# steve.left(90)
# steve.forward(75)
# steve.left(90)
# steve.pendown()
# steve.pencolor('gold')
# for i in range(4):
#     steve.forward(150)
#     steve.right(90)
#     steve.forward(25)
#     steve.right(90)
#     steve.forward(25)
#     steve.right(90)
#
# ben = turtle.Turtle()
# ben.shape('turtle')
# ben.color('royalblue')
# # ben.hideturtle()
# ben.speed(100)
# ben.pendown()
# ben.pencolor('LightBlue')
# for i in range(36):
#     ben.circle(100)
#     ben.left(10)
# ben.hideturtle()
# ben.left(90)
# ben.penup()
# ben.forward(200)
# ben.pendown()
# ben.write('Hello Little Turtle', move=False, align='center', font=("New Times Roman", 24, "bold"))



window.mainloop()
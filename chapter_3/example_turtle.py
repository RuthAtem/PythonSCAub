import turtle # Allows us to use turtles
window = turtle.Screen() # Creates a playground for turtles
color= None
while color is None:
    color =window.textinput("Please enter a background color for the screen","Color:")
# The textinput() method was introduced in Python 3 and 
# takes the console out of the interaction. 

window.bgcolor(color)
window.title("Hello, Alex")

alex = turtle.Turtle() # Create a turtle, assign to alex
color= None
while color is None:
    color =window.textinput("Please enter a color for the turtle","Color:")

alex.color(color)
alex.pensize(3)

alex.forward(50) # Tell alex to move forward by 50 units
alex.left(90) # Tell alex to turn by 90 degrees
alex.forward(70) # Complete the second side of a rectangle

window.mainloop() # Wait for user to close window

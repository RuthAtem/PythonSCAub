import turtle
window = turtle.Screen() # Sets up the window and its attributes 

color= None
while color is None:
    color =window.textinput("Please enter a background color for the screen","Color:")

window.bgcolor(color) 
window.title("Tess & Alex")
tess = turtle.Turtle() # Creates tess and set some attributes

color= None
while color is None:
    color =window.textinput("Please enter a color for tess","Color:")

tess.color(color) 
tess.pensize(3)

alex = turtle.Turtle() # Creates alex

color= None
while color is None:
    color =window.textinput("Please enter a color for alex","Color:")

alex.color(color) 
alex.pensize(5)

for i in range(3): 
    tess.forward(80)
    tess.left(120)

tess.right(180) # Turn tess around 
tess.forward(80)

for j in range(4):
    alex.forward(50)
    alex.left(90)

window.mainloop()

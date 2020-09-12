import turtle
window = turtle.Screen() # Sets up the window and its attributes 
window.bgcolor("lightgreen") 
window.title("Tess & Alex")
tess = turtle.Turtle() # Creates tess and set some attributes 
tess.color("blue") 
tess.pensize(3)

alex = turtle.Turtle() # Creates alex
alex.color("red") 
alex.pensize(5)

tess.forward(80) # Makes tess draw equilateral triangle
tess.left(120) 
tess.forward(80)
tess.left(120) 
tess.forward(80) 
tess.left(120) # Complete the triangle
tess.right(180) # Turn tess around 
tess.forward(80) # Move her away from the origin

alex.forward(50) # Make alex draw a square 
alex.left(90) 
alex.forward(50) 
alex.left(90)
alex.forward(50) 
alex.left(90)
alex.forward(50)
alex.left(90)
window.mainloop()

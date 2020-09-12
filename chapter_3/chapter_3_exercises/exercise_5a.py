import turtle # Allows us to use turtles
window = turtle.Screen() # Creates a playground for turtles
window.bgcolor("lightgreen")
window.title("Equilateral triangle")
meli = turtle.Turtle() # Creates Meli
meli.color("red") 
meli.pensize(3)

for i in range(3): 
    meli.forward(100)
    meli.left(120)

window.mainloop()
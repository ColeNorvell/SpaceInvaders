# Import the Tkinter & Turtle Graphics Modules
import Tkinter
import turtle

# Create Game Window
screen = turtle.Screen()
screen.screensize(500, 500, "black")

# Create Sprite
screen.addshape("Defender.gif")
mySprite = turtle.Turtle()
mySprite.hideturtle() # hide turtle until the the duck image replaces the placeholder shape
mySprite.penup() # prevent sprite from drawing on screen as it moves
mySprite.left(90) # rotate sprite for proper placement on screen
mySprite.shape("Defender.gif") # Set Image for Sprite
mySprite.setposition(0,-200)
mySprite.showturtle()

# Create Player Controls
def left():
    global mySprite
    mySprite.setposition(mySprite.xcor() - 10, mySprite.ycor())

def right():
    global mySprite
    mySprite.setposition(mySprite.xcor() + 10, mySprite.ycor())

def fire():
    print("FIRE! (space bar pressed)")

# Set Event Listeners for Player Controls
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(fire, "space")
screen.listen()

# Main Game Loop (Keeps Game Window From Closing)
Tkinter.mainloop()

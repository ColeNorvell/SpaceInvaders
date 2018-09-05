# Import the Tkinter & Turtle Graphics Modules
import Tkinter
import turtle

# Create Game Window
screen = turtle.Screen()
screen.screensize(500, 500, "black")

class Defender(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

class Invader(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

# Create Sprite
screen.addshape("Defender.gif")
defender = Defender()
defender.hideturtle() # hide turtle until the the defender replaces the placeholder shape
defender.penup() # prevent sprite from drawing on screen as it moves
defender.left(90) # rotate sprite for proper placement on screen
defender.shape("Defender.gif") # Set Image for Sprite
defender.setposition(0,-225)
defender.showturtle()

# Create Player Controls
def left():
    if defender.xcor() >= -225:
        global mySprite
        defender.setposition(defender.xcor() - 10, defender.ycor())

def right():
    if defender.xcor() <= 225:
        global mySprite
        defender.setposition(defender.xcor() + 10, defender.ycor())

def fire():
    print("FIRE! (space bar pressed)")

#add fire here?????????????

# Set Event Listeners for Player Controls
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(fire, "space")
screen.listen()

#Create enemy Sprites
screen.addshape("invader.gif")
invader = Invader()
invader.hideturtle()
invader.penup()
invader.left(90)
invader.shape("invader.gif")
invader.setposition(0,0)
invader.showturtle()

# Main Game Loop (Keeps Game Window From Closing)
Tkinter.mainloop()

#Create Laser

#Make it so Friendly Laser comes out of pilot when spacebar is pressed

#Make it so Friendly Laser kills Enemy Sprites

#Make it so killing all Enemy Sprites causes a refresh of enemies

#Attach point system to death of Enemy Sprites

#Make it so Enemy can create Lasers

#Make it so Enemy Lasers make the pilot lose

#Make it so losing makes "Game Over Appear"

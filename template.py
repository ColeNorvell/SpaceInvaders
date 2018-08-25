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
mySprite.setposition(0,-225)
mySprite.showturtle()

# Create Player Controls
def left():
    if mySprite.xcor() >= -225:
        global mySprite
        mySprite.setposition(mySprite.xcor() - 10, mySprite.ycor())

def right():
    if mySprite.xcor() <= 225:
        global mySprite
        mySprite.setposition(mySprite.xcor() + 10, mySprite.ycor())

def fire():
    print("FIRE! (space bar pressed)")
    
#add fire here?????????????

# Set Event Listeners for Player Controls
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(fire, "space")
screen.listen()


# Main Game Loop (Keeps Game Window From Closing)
Tkinter.mainloop()

#Create enemy Sprites
screen.addshape("invader.gif")
mySprite = turtle.Turtle()
mySprite.hideturtle()
mySprite.penup() 
mySprite.left(90)
mySprite.shape("invader.gif") 
mySprite.setposition(0,200)
mySprite.showturtle()
#Create Laser
if screen.onkey == ("space")
  #edit this, its wrong  
#Make it so Friendly Laser comes out of pilot when spacebar is pressed

#Make it so Friendly Laser kills Enemy Sprites

#Make it so killing all Enemy Sprites causes a refresh of enemies

#Attach point system to death of Enemy Sprites 

#Make it so Enemy can create Lasers

#Make it so Enemy Lasers make the pilot lose

#Make it so losing makes "Game Over Appear"

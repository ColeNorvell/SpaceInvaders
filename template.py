# SpaceInvaders.py by Cole Norvell & Chris Pedersen

# Import the Tkinter & Turtle Graphics Modules
import Tkinter
import turtle

# Create Game Window
screen = turtle.Screen()
screen.screensize(500, 500, "black")

# Load Images
screen.addshape("Defender.gif")
screen.addshape("Lazer.gif")


class Defender(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

class Shield(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

class Invader(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

class Lazer(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        '''
        this.hideturtle() # hide turtle until the the defender replaces the placeholder shape
        this.penup() # prevent sprite from drawing on screen as it moves
        this.left(90) # rotate sprite for proper placement on screen
        this.shape("Lazer.gif") # Set Image for Sprite
        this.setposition(0,0)
        this.showturtle()
        '''

# Create Sprite
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

lazer = []
lazerIndex = -1
def fire():
    global lazerIndex
    lazerIndex = lazerIndex + 1
    lazer.append(Lazer())
    lazer[lazerIndex].hideturtle() # hide turtle until the the defender replaces the placeholder shape
    lazer[lazerIndex].penup() # prevent sprite from drawing on screen as it moves
    lazer[lazerIndex].left(90) # rotate sprite for proper placement on screen
    lazer[lazerIndex].shape("Lazer.gif") # Set Image for Sprite
    lazer[lazerIndex].setposition(0,0)
    lazer[lazerIndex].showturtle()


# Set Event Listeners for Player Controls
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(fire, "space")
screen.listen()

#Create enemy Sprites
screen.addshape("invader.gif")

firstRowInvader = []
for i in range(7):
    firstRowInvader.append(Invader())
    if i == 0:
        x = 225
    else:
        x = x - 75
    firstRowInvader[i].hideturtle()
    firstRowInvader[i].penup()
    firstRowInvader[i].left(90)
    firstRowInvader[i].shape("invader.gif")
    firstRowInvader[i].setposition(x, 0)
    firstRowInvader[i].showturtle()

secondRowInvader = []
for i in range(7):
    secondRowInvader.append(Invader())
    if i == 0:
        x = 225
    else:
        x = x - 75
    secondRowInvader[i].hideturtle()
    secondRowInvader[i].penup()
    secondRowInvader[i].left(90)
    secondRowInvader[i].shape("invader.gif")
    secondRowInvader[i].setposition(x, 75)
    secondRowInvader[i].showturtle()

thirdRowInvader = []
for i in range(7):
    thirdRowInvader.append(Invader())
    if i == 0:
        x = 225
    else:
        x = x - 75
    thirdRowInvader[i].hideturtle()
    thirdRowInvader[i].penup()
    thirdRowInvader[i].left(90)
    thirdRowInvader[i].shape("invader.gif")
    thirdRowInvader[i].setposition(x, 150)
    thirdRowInvader[i].showturtle()

screen.addshape("Shield.gif")
shield = []
shieldx = -150
for i in range(3):
  shield.append(Shield())
  shield[i].hideturtle()
  shield[i].penup()
  shield[i].left(90)
  shield[i].shape("Shield.gif")
  shield[i].setposition(shieldx, -125)
  shield[i].showturtle()
  shieldx = shieldx + 150

#Create Laser

#Make it so Friendly Laser comes out of pilot when spacebar is pressed

#Make it so Friendly Laser kills Enemy Sprites

#Make it so killing all Enemy Sprites causes a refresh of enemies

#Attach point system to death of Enemy Sprites

#Make it so Enemy can create Lasers

#Make it so Enemy Lasers make the pilot lose

#Make it so losing makes "Game Over Appear"

# Main Game Loop (Keeps Game Window From Closing)
Tkinter.mainloop()

# Projectile Simulation with Plotting
# J. Matthew Myers
# January 6, 2022
# Distributed under the terms of the GNU GPLv3 license.

# This program utilizes the graphics.py written by John Zelle.
# graphics.py is open-source and released under the terms of the GPL.
# For more information about the graphics library, see the contents
# of graphics.py.

from projectile import *
from graphics import *
from button import Button

# getInputs
# Returns user-inputted values for launch angle, velocity, and sets the starting height and time to 0 and 0.1
def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = 0.0 # Fix initial height at 0.0
    t = 0.01 # Fix initial time interval at 0.01 sec
    return a, v, h, t

# makeButtons
# Takes the graphical window object as an argument
# Returns the Button objects to be used in the graphical window
def makeButtons(win):
    # Create buttons Button(win, center, width, height, label)
    fire = Button(win, Point(100,900), 155, 40, "Fire")
    fire.activate()
    aPlus5 = Button(win, Point(100,850), 155, 40, "Angle+5")
    aPlus5.activate()
    aMinus5 = Button(win, Point(100,800), 155, 40, "Angle-5")
    aMinus5.activate()
    vPlus5 = Button(win, Point(100,750), 155, 40, "Velocity+5")
    vPlus5.activate()
    vMinus5 = Button(win, Point(100,700), 155, 40, "Velocity-5")
    vMinus5.activate()
    _quit = Button(win, Point(100,650), 155, 40, "Quit")
    _quit.activate()

    return fire, aPlus5, aMinus5, vPlus5, vMinus5, _quit

# _fire
# Takes the graphical window object, the angle, velocity, initial height, and starting time as arguments
# Returns nothing
def _fire(win, angle, velocity, h0, time):
    # Cannonball object
    cball = Projectile(angle, velocity, h0)

    # Draw cannonball in initial position
    dot = Circle(Point(0,h0), 10)
    dot.setFill("red")
    dot.draw(win)

    # fire loop
    maxY = h0
    while (cball.getY() >= 0):
        oldX = cball.getX()
        oldY = cball.getY()
        cball.update(time)
        Point(cball.getX(), cball.getY()).draw(win)
        dot.move(cball.getX()-oldX, cball.getY()-oldY)
        if cball.getY() > maxY:
            maxY = cball.getY()

# Increases the launch angle by 5
def anglePlus5(angle):
    angle += 5
    return angle

# Decreases the launch angle by 5
def angleMinus5(angle):
    angle -= 5
    return angle

# Increases the launch velocity by 5
def velocityPlus5(velocity):
    velocity += 5
    return velocity

# Decreases the launch velocity by 5
def velocityMinus5(velocity):
    velocity -= 5
    return velocity

# Closes the window
def quit_(win):
    win.close()

def main():
    # Get inputs
    angle, velocity, h0, time = getInputs()

    # Open graphics window
    screenWidth = 640
    screenHeight = 480
    win = GraphWin("Projectile Trajectory", screenWidth, screenHeight)
    win.setBackground("white")

    # Define world coordinate system
    win.setCoords(-20, -20, 1260 ,940)

    # Draw axes
    Line(Point(0, 0), Point(1240, 0)).draw(win)
    Line(Point(0, 0), Point(0, 920)).draw(win)

    # Make buttons
    fire, aPlus5, aMinus5, vPlus5, vMinus5, _quit = makeButtons(win)

    # Display angle
    angleMessage = Text(Point(screenWidth / 2, 2 * screenHeight - 40), ("Angle = {}".format(angle)))
    angleMessage.draw(win)

    #  Display velocity
    velocityMessage = Text(Point(screenWidth, 2 * screenHeight - 40), ("Velocity = {}".format(velocity)))
    velocityMessage.draw(win)

    # Fire first cannonball
    _fire(win, angle, velocity, h0, time)

    # Flight data output
    #print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    #print("Maximum height: {0:0.1f} meters ".format(maxY))

    # Main loop
    while True:
        # Get mouse position
        pt = win.getMouse()
        
        # Handle button clicks
        if fire.clicked(pt):
            _fire(win, angle, velocity, h0, time)
        if aPlus5.clicked(pt):
            angle = anglePlus5(angle)
        if aMinus5.clicked(pt):
            angle = angleMinus5(angle)
        if vPlus5.clicked(pt):
            velocity = velocityPlus5(velocity)
        if vMinus5.clicked(pt):
            velocity = velocityMinus5(velocity)
        if _quit.clicked(pt):
            quit_(win)

        # Display current angle and velocity
        angleMessage.setText(("Angle = {}".format(angle)))
        velocityMessage.setText(("Velocity = {}".format(velocity)))

main()








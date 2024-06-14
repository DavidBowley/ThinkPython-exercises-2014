from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print bob

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)
        
def polygon(t, length, n, angle):
    percentage = round((angle / 360.0) * 100)
    decimal_percentage = percentage / 100
    for i in range(int(round(n * decimal_percentage))):
        fd(t, length)
        lt(t, 360.0/n)

def circle(t, r):
    """ Function takes a Turtle as t, and radius of circle as r
    """
    circumference = 2 * math.pi * r
    polygon(t, 1, int(round(circumference)))
        
def arc(t, r, angle):
    circumference = 2 * math.pi * r
    polygon(t, 1, int(round(circumference)), angle)

arc(bob, 50, 270)
    
wait_for_user()


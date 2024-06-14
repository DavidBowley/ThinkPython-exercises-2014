"""File:     draw_circle.py
   Purpose:  Use the TurtleWorld module in Swampy to draw a circle.

   Run:      python draw_circle.py

   Input:    None, except to terminate the program, click X to close the 
             window
   Output:   A window with a square in it
"""

from swampy.TurtleWorld import *
from math import pi

#----------------------------------------------------------------------
def draw_polygon(t, length, n):  
   """Draw a regular polygon with n sides and sidelength length
      using turtle t
   """
   degrees = 360.0/n;            
   for i in range(n):
      fd(t, length)
      lt(t, degrees)

#----------------------------------------------------------------------
def draw_circ(t, r):      
   """Draw a circle with radius r using turtle t
   """
   circumference = 2*pi*r
   n = int(round(circumference))
   draw_polygon(t, 1, n)

#----------------------------------------------------------------------
# Program starts here
world = TurtleWorld() # Create an instance of TurtleWorld -- i.e, a window
bob = Turtle()        # Create an instance of a Turtle
bob.delay = 0.01

r = int(raw_input("What's the circle's radius?\n   "))

draw_circ(bob, r)

wait_for_user()
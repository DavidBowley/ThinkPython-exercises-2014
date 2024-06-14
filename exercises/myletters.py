from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print bob

def draw_a(t):
    lt(t, 70)
    fd(t, 50)
    rt(t, 140)
    fd(t, 50)
    rt(t, 110)
    fd(t, 50)
    
draw_a(bob)

wait_for_user()
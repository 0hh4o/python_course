import math
def bouncing_ball(h, bounce, window):
    n = int(math.log(window,bounce*h))
    t = 2*n -1
    return t
bouncing_ball(20,0.5,1)
import math
def bouncing_ball(h, bounce, window):
    n = int(math.log(window,bounce*h))
    t = 2*n -1
    print(t)
bouncing_ball(20,0.5,1)
import math
def bouncing_ball(h, bounce, window):
    n = int(math.log(window,bounce*h))
    t = 2*n -1
<<<<<<< HEAD
    print(t)
=======
    return t
>>>>>>> 8f865c1e51719b818884819f273595440f3b4800
bouncing_ball(20,0.5,1)
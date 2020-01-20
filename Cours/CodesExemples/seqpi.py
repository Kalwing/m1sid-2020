import numpy as np
import time
def picks(n):
    count_inside=0
    for i in range(n):
        x,y=np.random.random(2)*2-1
        if x*x+y*y <=1: count_inside+=1
    return count_inside

def compute_pi(n):
    return 4*picks(n)/n


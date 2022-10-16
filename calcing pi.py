import numpy as np
import random
import matplotlib.pyplot as plt
#max_length = np.sqrt(2*radius**2)

def pie(k,r):
    i = 0
    j = 0
    for t in np.arange(0,k+1):
        x = random.uniform(0,r)
        y = random.uniform(0,r)
        h = np.sqrt(x * x + y * y)
        #print(l)
        if h > r:
            j += 1
        else:
            i += 1
            j += 1
    pie_1 = 4 * (i/j)
    #print(pie_1)
    return pie_1

# print(pie(10,1))
# print(pie(100000,1))

def draw_error(k,r):
    u = []
    for t in np.arange(0,k+1):
        l = pie(k, r)
        u.append(abs(np.pi-l))
    f  = np.arange(1,len(u)+1)
    plt.plot(f,u)
    #print(u)

print(pie(33333,4))
        
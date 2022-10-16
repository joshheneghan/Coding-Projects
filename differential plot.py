import numpy as np
import matplotlib.pyplot as plt
w = 1 #Omega
a = -10000
b = 100000
Ip = []
h1 = []
err = []
def f(x):
    return ((w/np.pi)**0.25)*(np.e**((-w*x**2)/2)) #Phi0


for n in range(2,10,2): #Running 2-8
    h1 = []
    err = []
    Ip = []
    y = []
    for t in range(1,11,1):
        a = -10
        b = 11
        h = abs((b-a) / t)
        h1.append(h)
        for x in np.arange(-10,11,h): #Looping for all trapezoids
            u = []
            co = []
            for j in range(0,n+1): #Code for L'' values
                        sum__ = 0
                        for i in range(0,n+1):
                            sum_=0
                            if i != j:
                                for m in range(0,n+1):
                                    prod = 1
                                    if m != j and m != i:
                                        for l in range(0,n+1):
                                            if l != m and l != j and l != i:
                                                prod *= (0.5*n-l)/(j-l)
                                            else:
                                                pass   
                                        sum_ += prod/(j-m)
                                    else:
                                        pass 
                                sum__ += sum_/(j-i)
                            else:
                                pass
                        co.append(sum__) #Appending empty array                            
            p = len(co)
            p_ = int(0.5-(p/2)) #Used to get Li
            ssum = 0
            for c in range(p_,abs(p_)+1):
                d = f((x)+c*h)
                u.append(d)
                    
            for b in range(0,p):
                ssum += (co[b]*u[b])/h**2
            final_sum=(-0.5*ssum+(0.5*(w**2)*(x)**2)*f(x))*f(x) #Multiplying our value of the second derivative by -0.5 and the additional term of phi
            Ip.append(final_sum)
            #print(final_sum)
            S = sum(Ip)
        y.append(h*S)
        err.append(abs(h*S - 0.5))
        plt.semilogy(h1,err)

plt.legend(["n=2","n=4","n=6","n=8"])     
plt.title("The Error in the Result for the Energy of a Quantum State")   
plt.xlabel("h values")
plt.ylabel("Log of the Error")
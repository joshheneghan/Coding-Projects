#Defining the function and its derivative as well as the boundaries
def f(x):
    return (x-1)*(x-2)*(x-3)*(x-4)

def dfdx(x):
    return 4*x**3 - 30*x**2 + 70*x - 50

eps = 1*10**-15
 #%%
# Bisection
print(
      "Bisection"
      )

z = 0
a = 0.8 # Initial lower absbound
b = 1.1 # Initial upper bound

# Loop whiles b - a is bigger than eps, chosen to be small

while abs(b - a) > eps:
    z +=1
    # find xmid
    c = (a+b)/2
    print(c)
    # Evaluate at xmid. If it's larger than zero move the upper bound down
    if f(c)*f(b) > 0:
        b = c
    # else move the lower bound up
    else:
        a = c

print(z)
    
#%%
# Newtons Method
print(
      "Newton"
      )
z = 0
a = 3.8 # Initial lower bound
b = 4.1 # Initial upper bound
while abs(f(a))>eps:
    z +=1
    print(a)
    a = a - f(a)/dfdx(a)
    
print(z)
#%%
# Secant
print(
      "Secant"
      )
z = 1
a = 0.8 # Initial lower bound
b = 1.1 # Initial upper bound
c = b - f(b)*((b-a)/(f(b)-f(a)))
print(c)
while abs(f(c)) > eps:
    
    z +=1
    # c
    c = b - f(b)*((b-a)/(f(b)-f(a)))
    
    # Evaluate at xmid. If it's larger than zero move the upper bound down
    if f(c) > 0:
        b = c
    # else move the lower bound up
    else:
        a = c

    # print the midpoint
    print(c)

print(z)
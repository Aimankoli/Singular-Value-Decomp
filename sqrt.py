import numpy as np
sqrt=-0.001

precision = 100
ctr=0

current=sqrt
def function(x):
    return x**3 -x

def fprime(x):
    return 3*(x**2) -1
while (ctr<precision):
    x=function(current)
    xprime=fprime(current)
    current = current - x/xprime
    ctr+=1
    # print(current)

print (current)

//iterate for whhich values it goes to 0 and for which it goes to 1
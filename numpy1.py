#!/usr/bin/python36
import numpy as np

a=np.array([2,3,6,7]) #single dimensional array
print(a)
b=np.array([3,5,7,8]) # single dimensional array
print(b)

c=a+b   # addition of array a and b
print(c)

d=a*b
print(d)  #multiplication od array a and b

e=a**2
print(e)  #square of array a

f=a**3
print(f) #cube of array a

g=a[3]    # give a particular element of a array
print(g)

h=a+2   # add 2 with all elements of array
print(h)

#!/usr/bin/python36
import numpy as np

a=np.array([[2,3,4],[5,6,7]]) #two dimensional array
print(a)

b=np.array([[5,5],[3,6],[4,9],[7,8]]) #two dimensional array
print(b)

c1=a.shape   #show total no of rows and column
print(c1)  
c2=b.shape   #show total no of rows and column
print(c2)

d1=a**2
print(d1)
d2=b**3
print(d2)

#operation on array b

e1=b[0:]
print(e1)

e2=b[[0,3],0:]
print(e2)

e3=b[0:,1]  # or we can write b[0:,1:]
print(e3)

e4=b[[0,3],1]
print(e4)

#operation on array a

f1=a[0:]
print(f1)

f2=a[0:,[0,2]]
print(f2)

f3=a[0,[0,1]]
print(f3)

f4=a[1,2]
print(f4)

#some other operation

g1=np.zeros((3,6))
print(g1)

g2=np.ones((4,5))
print(g2)

g3=np.full((3,6),7)
print(g3)




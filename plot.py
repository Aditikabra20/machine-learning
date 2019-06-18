#!/usr/bin/python36
import matplotlib.pyplot as plt

x=[2,3]
y=[5,9]
x1=[6,8,4]
y1=[5,4,7]

plt.xlabel("time")     # time on x-axis
plt.ylabel("velocity")  # velocity on y-axis

plt.plot(x,y,label="water") #this will show a straight line ,show line with a label
plt.bar(x,y)  #plot bat graph
plt.plot(x1,y1,label="sand") #this wiil show a straight line,show line with a label
plt.bar(x1,y1)  #plot bar graph

plt.grid(color="red") # form grid in graph
plt.legend() # show label with plot
plt.xlim(0,10)
plt.ylim(0,10)  # show min and max number on y-axis
plt.show()




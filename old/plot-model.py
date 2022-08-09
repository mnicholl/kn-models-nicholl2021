import numpy as np
import json
import matplotlib.pyplot as plt
import sys

plt.figure(1)
plt.clf()

if len(sys.argv)>1:
    i = sys.argv[1]

d = np.genfromtxt(i)


plt.plot(d[:,0],d[:,1]+7,color='blueviolet')
plt.plot(d[:,0],d[:,2]+5,color='mediumslateblue')
plt.plot(d[:,0],d[:,3]+5,color='cadetblue')
plt.plot(d[:,0],d[:,4]+4,color='midnightblue')
plt.plot(d[:,0],d[:,5]+2,color='g')
plt.plot(d[:,0],d[:,6]+0,color='r')
plt.plot(d[:,0],d[:,7]-1,color='y')
plt.plot(d[:,0],d[:,8]-2,color='k')
plt.plot(d[:,0],d[:,9]-3,color='hotpink')
plt.plot(d[:,0],d[:,10]-4,color='peru')
plt.plot(d[:,0],d[:,11]-5,color='brown')
plt.plot(d[:,0],d[:,12]-6,color='orange')



plt.gca().invert_yaxis()

plt.xlabel('Days')

plt.ylabel('Magnitude')

plt.tight_layout(pad=0.5)

plt.show()

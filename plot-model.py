import numpy as np
import matplotlib.pyplot as plt
import sys


plt.figure(1)
plt.clf()

if len(sys.argv)>1:
    i = sys.argv[1]

d = np.genfromtxt(i)


plt.plot(d[:,0],d[:,1]+8,color='blueviolet')
plt.plot(d[:,0],d[:,2]+7,color='mediumslateblue')
plt.plot(d[:,0],d[:,3]+6,color='cadetblue')
plt.plot(d[:,0],d[:,4]+5,color='midnightblue')
plt.plot(d[:,0],d[:,5]+4,color='b')
plt.plot(d[:,0],d[:,6]+3,color='g')
plt.plot(d[:,0],d[:,7]+2,color='lightgreen')
plt.plot(d[:,0],d[:,8]+1,color='c')
plt.plot(d[:,0],d[:,9]+0,color='r')
plt.plot(d[:,0],d[:,10]-1,color='firebrick')
plt.plot(d[:,0],d[:,11]-2,color='orange')
plt.plot(d[:,0],d[:,12]-3,color='gold')
plt.plot(d[:,0],d[:,13]-4,color='k')
plt.plot(d[:,0],d[:,14]-5,color='hotpink')
plt.plot(d[:,0],d[:,15]-6,color='peru')
plt.plot(d[:,0],d[:,16]-7,color='brown')
plt.plot(d[:,0],d[:,17]-8,color='orange')


plt.gca().invert_yaxis()

plt.xlabel('Days')

plt.ylabel('Magnitude')

plt.tight_layout(pad=0.5)

plt.show()

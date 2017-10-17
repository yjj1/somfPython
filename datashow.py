# -*- coding:'utf8' -*-
#encoding=utf-8
from urllib import *
import urllib2
from numpy import genfromtxt, zeros
from pylab import plot, show
from pylab import figure, subplot, hist, xlim, show
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urllib2.urlopen(url)
localFile = open('iris.csv', 'wb+')
localFile.write(u.read())
localFile.close()

data = genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))

target = genfromtxt('iris.csv', delimiter=',', usecols=4, dtype=str)

print data.shape
print target.shape

print set(target)

plot(data[target=='setosa', 0], data[target=='setosa', 2], 'bo')
plot(data[target=='versicolor', 0], data[target=='versicolor', 2], 'ro')
plot(data[target=='virginica', 0], data[target=='virginica', 2], 'go')
show()

xmin = min(data[:,0])
xmax = max(data[:,0])
figure()
subplot(411) # distribution of the setosa class (1st, on the top)
hist(data[target=='setosa',0],color='b',alpha=.7)
xlim(xmin,xmax)
subplot(412) # distribution of the versicolor class (2nd)
hist(data[target=='versicolor',0],color='r',alpha=.7)
xlim(xmin,xmax)
subplot(413) # distribution of the virginica class (3rd)
hist(data[target=='virginica',0],color='g',alpha=.7)
xlim(xmin,xmax)
subplot(414) # global histogram (4th, on the bottom)
hist(data[:,0],color='y',alpha=.7)
xlim(xmin,xmax)
show()

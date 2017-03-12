# -*- coding: utf-8 -*-
import numpy as np
import pylab

xulie_list = []
xulie_file = open('AR序列.txt')
for e in xulie_file:
    xulie_list.append(float(e.strip('\n')))
xulie_file.close()

p = [0]*len(xulie_list)
p[0] = 10**5
sita = [0]*len(xulie_list)
em = [0]*len(xulie_list)
tao = [0]*len(xulie_list)

for i in xrange(1,len(xulie_list)):
    sita[i] = sita[i-1]+((p[i-1]*xulie_list[i-1])/(
        1+xulie_list[i-1]*p[i-1]*xulie_list[i-1]))*(
        xulie_list[i]-xulie_list[i-1]*sita[i-1])

    p[i] = p[i-1]-(p[i-1]*xulie_list[i-1]*xulie_list[i-1]*p[i-1])/(
        1+xulie_list[i-1]*p[i-1]*xulie_list[i-1])

print sita[len(xulie_list)-1]

for i in xrange(1,len(xulie_list)):
    em[i] = xulie_list[i]-xulie_list[i-1]*sita[i-1]

tao[1] = em[1]**2

for i in xrange(2,len(xulie_list)):
    tao[i] = tao[i-1]+(em[i]**2-tao[i-1])/i


  
pylab.figure()
pylab.plot(sita,'k-',label='canshu')
#pylab.plot(tao,'k-',label='fangcha')
pylab.legend()
pylab.show()

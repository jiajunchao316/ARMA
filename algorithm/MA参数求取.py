# -*- coding: cp936 -*-
import numpy as np

xulie_list = []
xulie_file = open('误差2.txt')
for e in xulie_file:
    xulie_list.append(float(e.strip('\n')))
xulie_file.close()

p = [0]*len(xulie_list)
p[9] = 10**5*np.eye(10)
sita = [np.matrix([[0],[0],
                  [0],[0],
                  [0],[0],
                  [0],[0],
                  [0],[0]])]*len(xulie_list)

for i in xrange(10,len(xulie_list)):
    fai = np.matrix([[-xulie_list[i-1]],[-xulie_list[i-2]],[-xulie_list[i-3]],
                     [-xulie_list[i-4]],[-xulie_list[i-5]],[-xulie_list[i-6]],
                     [-xulie_list[i-7]],[-xulie_list[i-8]],[-xulie_list[i-9]],
                     [-xulie_list[i-10]]])
    sita[i] = sita[i-1]+((p[i-1]*fai)/(
            1+fai.T*p[i-1]*fai))*(xulie_list[i]-fai.T*sita[i-1])
    p[i] = p[i-1]-(p[i-1]*fai*fai.T*p[i-1])/(1+fai.T*p[i-1]*fai)

    res = sita[i]

B = np.matrix([[1,0,0],
               [res[0],1,0],
               [res[1],res[0],1],
               [res[2],res[1],res[0]],
               [res[3],res[2],res[1]],
               [res[4],res[3],res[2]],
               [res[5],res[4],res[3]],
               [res[6],res[5],res[4]],
               [res[7],res[6],res[5]],
               [res[8],res[7],res[6]],
               [res[9],res[8],res[7]],
               [0,res[9],res[8]],
               [0,0,res[9]]])
b = np.matrix([[-res[0]],[-res[1]],[-res[2]],[-res[3]],[-res[4]],
               [-res[5]],[-res[6]],[-res[7]],[-res[8]],[-res[9]],
               [0],[0],[0]])

res_ma = np.linalg.inv((B.T*B))*B.T*b
print res_ma

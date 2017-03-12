# -*- coding: utf-8 -*-
#Get the parameter characteristics of the sequence  

import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

data_list = []
e_list = []
ee_list = []
class ARMA(object):
    def __init__(self,z,n):
        super(ARMA,self).__init__()
        self.z = z
        self.n = n
        self.z_are = 0
        self.z_std = 0
        self.rk = 0
        self.pk = 0
        self.pk_list = []
        self.prk_list = []
        self.R = 3*[0]
        self.Rr = np.zeros

    def draw(self):
        xlabel(u'时延')
        ylabel(u'自相关函数')
        axhline(0)
        plot(self.pk_list,'bo',label = u'自相关函数')
        plot(self.prk_list,'ro',label = u'偏自相关') 
        plt.show()

    def characteristic_par(self):
        self.are_and_std()
        self.sampled_correlaton_par()
        self.p_sampled_correlaton_par()
        self.MA()

    def are_and_std(self):
        N = self.n
        z_sum = 0
        z_std_sum = 0
        for i in xrange(N):
            z_sum = z_sum+self.z[i]
        self.z_are = z_sum/N
        print 'z_are---',self.z_are

        for i in xrange(N):
            z_std_sum = z_std_sum + (self.z[i]-self.z_are)**2
        self.z_std = z_std_sum/N
        print 'z_std---',self.z_std

    def sampled_correlaton_par(self,k=0):
        N = self.n
        rk_sum = 0
        for i in xrange(N-k):
            rk_sum = rk_sum + (self.z[i]-self.z_are)*(self.z[i+k]-self.z_are)
        self.rk = rk_sum/N
        self.pk = self.rk/self.z_std
        self.pk_list.append(self.pk)
        print 'r%d------'%k,self.rk
        print 'p%d------'%k,self.pk
        k = k+1
        if k < 15:
            return self.sampled_correlaton_par(k)
        
        self.draw()

    def p_sampled_correlaton_par(self,k=2):
        '''
        N = len(self.pk_list)
        dat_t = 0
        dat_b = 0
        self.prk_list = np.zeros((self.n,self.n))
        for i in xrange(1,N):
            if i == 1:
                self.prk_list[1][1] = self.pk_list[1]
                continue
            for j in xrange(1,i):
                dat_t = dat_t+self.prk_list[i-1][j]*self.pk_list[i-j]
                dat_b = dat_b+self.prk_list[i-1][j]*self.pk_list[j]
            self.prk_list[i][i] = (self.pk_list[i]-dat_t)/(1-dat_b)
            for k in xrange(1,i):
                self.prk_list[i][k] = self.prk_list[i-1][k]-self.prk_list[i][i]*self.prk_list[i-1][i-k]
        print '偏自相关参数矩阵\n',self.prk_list
        '''

        m = np.zeros((k-1,k-1))
        n = np.zeros(k-1)
        ml = []
        nl = []
        
        for i in range(1,k):
            for j in range(1,k):
                m[i-1][j-1] = self.pk_list[abs(i-j)]
            n[i-1] = self.pk_list[i]
        for s in range(k-1):
            ml.append(list(m[s]))
            nl.append(float(n[s]))

        mm = np.matrix(ml)
        nn = np.matrix([nl]).T


        res = float((np.linalg.inv(mm)*nn)[k-2])
        self.prk_list.append(res)

        k +=1
        if k < len(self.pk_list)+1:
            return self.p_sampled_correlaton_par(k)

        self.draw()

    def MA(self):
        N = len(data_list)
        for i in range(2):
            s = 0
            for j in range(i,N):
                s = s+data_list[j]*data_list[j-i]
            self.R[i] = s/N

        print self.R[0],self.R[1]/self.R[0]
        

            
f = open('误差1.txt')
for d in f:
    data_list.append(float(d.strip('\n').split()[0]))
f.close()
for i in range(1,len(data_list)):
    e_list.append(data_list[i]-data_list[i-1])
for i in range(1,len(e_list)):
    ee_list.append(e_list[i]-e_list[i-1])
arma = ARMA(data_list,len(data_list))
arma.characteristic_par()




    
        
        

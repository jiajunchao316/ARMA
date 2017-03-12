# -*- coding: utf-8 -*-
import numpy as np
from pylab import*
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

class modle(object):
    def __init__(self):

        self.result = []
        self.Q = np.matrix([[0.5,0,0,0],
               [0,3.5,0,0],
               [0,0,3.5,0],
               [0,0,0,3.5]])
        self.R = np.matrix([[0.01]]) 
        self.xhat = np.matrix([[11.463],[0],[-0.0108],[0.029]])
        self.P = 10*np.eye(4)
        self.A = np.matrix([[1,0,0,0],
                  [0,-0.575,0,0],
                  [0,0,-0.493,0],
                  [0,0,0,0.221]])
        self.H = np.matrix([[1,1,0,0]])
        self.I = np.eye(4)
        self.z = []
        self.sf = open('优点3.txt','w')
        self.readfile()

    def draw(self):
        plot(self.z,'k-',label='noisy measurements')     
        plot(self.result,'r-')
        #ylim(-0.8,0.6)
        ylabel(u'伪距/m')
        plt.show()

    def KF(self,r):
        z = np.matrix([[r]])
        xm = self.A*self.xhat
        pm = self.A*self.P*self.A.T+self.Q

        error = z - self.H*xm
        K = pm*self.H.T*np.linalg.inv((self.H*pm*self.H.T+self.R))
        self.xhat = xm + K*error
        self.P = (self.I-K*self.H)*pm

        self.result.append('%0.4f'%float(self.xhat[0]))
        self.sf.write('%0.4f'%float(self.xhat[0])+'\n')

    def readfile(self):
        f = open('点3.txt')
        for d in f:
            r = float(d.strip('\n'))
            self.z.append(float(d.strip('\n')))
            self.KF(r)
        f.close()
        self.sf.close()
        self.draw()

modle()

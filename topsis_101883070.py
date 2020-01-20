# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:25:13 2020

@author: Vanshita
"""
import math
import pandas as pd


class Topsis:
    def init(self,file):
        data = pd.read_csv(file)
        self.d = data.iloc[:,:].values
        self.d = self.d.astype("float64")
        self.features = len(self.d[0])
        self.samples = len(self.d)
    def function(self,a):
        return a[1]
    def func(self,a):
        return a[0]
 
    def evaluate(self,w = None,im = None): 
        d = self.d
        features = self.features
        samples = self.samples
        if w==None:
            w=[1]*features
        if im==None:
            im=["+"]*features
        ideal_best=[]
        ideal_worst=[]
        for i in range(0,features):
            k = math.sqrt(sum(d[:,i]*d[:,i]))
            maxi = 0
            mini = 1 
            for j in range(0,samples):
                d[j,i] = (d[j,i]/k)*w[i]
                if d[j,i]>maxi:
                    maxi = d[j,i]
                if d[j,i]<mini:
                    mini = d[j,i]
            if im[i] == "+":
                ideal_best.append(maxi)
                ideal_worst.append(mini)
            else:
                ideal_best.append(mini)
                ideal_worst.append(maxi)
        gh = []
        for g in range(0,samples):
            a1 = math.sqrt(sum((d[g]-ideal_worst)*(d[g]-ideal_worst)))
            b1 = math.sqrt(sum((d[g]-ideal_best)*(d[g]-ideal_best)))
            lst = []
            lst.append(g)
            lst.append(a1/(a1+b1))
            gh.append(lst)
        gh.sort(key=self.function)
        r = 1
        for i in range(samples-1,-1,-1):
            gh[i].append(r)
            r+=1
        gh.sort(key=self.func)
        return gh
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 00:19:01 2020

@author: 爱动脑的小王欣
"""

from manimlib.imports import *
import numpy as np


def rack(x, a=20, m=1):
    x = x % (np.pi*m)
    k = np.tan((90-a)/180*np.pi)
    tr = np.array([np.pi/4-1/k, np.pi/4+1.25/k, np.pi*3/4-1.25/k, np.pi*3/4+1/k])*m
    y = []
    for xi in x.flat:
        if xi<tr[0]:
            yi = m
        elif tr[0]<=xi and xi<tr[1]:
            yi=k*np.pi/4*m-k*xi
        elif tr[1]<=xi and xi<tr[2]:
            yi = -1.25*m
        elif tr[2]<=xi and xi<tr[3]:
            yi = -k*np.pi*3/4*m+k*xi
        elif tr[3]<=xi:
            yi = m
        y.append(yi+1.1)
    return y



class chi(Scene):
    def construct(self):
        j=np.arange(0,360,3)
        r=np.sin(10*j/180*PI)+3
        print(j)
        print(r)
        x=[]
        y=[]
        for i in range(len(r)):
            x.append(r[i]*np.cos(j[i]/180*PI))
            y.append(r[i]*np.sin(j[i]/180*PI))

        d=[]
        for i in range(len(x)):
            p=Dot()
            p.move_to(UP*y[i]+RIGHT*x[i])
            d.append(p)
        for i in d:
            self.play(FadeIn(i))
        self.wait(1)
        
'''
        cd /d E:
cd E:\Strict\manim-master
python manim.py chi.py -pl
'''
class chi_example(Scene):
    def set_chi(self,rad):
        print()
    def construct(self): 
        c1=Circle()
        j=np.linspace(0,2*PI*10,360)
        #a=10,m=3  6瓣子母花
        r=rack(j/6,a=30,m=1)

        x=[]
        y=[]
        for i in range(len(r)):
            r[i]=r[i]+1
            x.append(r[i]*np.cos(j[i]/10))
            y.append(r[i]*np.sin(j[i]/10))
        d1=[]    
        for i in range(1,len(r)):
            p1=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])
            d1.append(p1)

        self.play(FadeIn(c1))
        for i in d1:
            self.play(FadeIn(i))

        for p in range(10):
            for i in d1:
                i.rotate(PI/180,about_point=[0,0,0])
            self.wait(1)
            if p%20==0:
                print(p)
class chi2(Scene):
    def construct(self):
        c=[]
        for i in range(9):
            c1=Circle()
            c1.scale(2)
            c.append(c1)
        c[1].move_to(RIGHT*8.7+DOWN*8.7)
        c[2].move_to(RIGHT*8.7)
        c[3].move_to(UP*8.7)
        c[4].move_to(DOWN*8.7)
        c[5].move_to(LEFT*8.7)
        c[6].move_to(RIGHT*8.7+UP*8.7)
        c[7].move_to(LEFT*8.7+UP*8.7)
        c[8].move_to(LEFT*8.7+DOWN*8.7)
        j=np.linspace(0,2*PI*10,360)
        r=rack(j/2)
        L1=Line(RIGHT*8.7+DOWN*8.7,LEFT*8.7+DOWN*8.7,stroke_width=20)
        L2=Line(RIGHT*8.7+UP*8.7,LEFT*8.7+UP*8.7,stroke_width=20)
        L3=Line(RIGHT*8.7+UP*8.7,RIGHT*8.7+DOWN*8.7,stroke_width=20)
        L4=Line(LEFT*8.7+DOWN*8.7,LEFT*8.7+UP*8.7,stroke_width=20)
        L5=Line(RIGHT*8.7+DOWN*8.7,LEFT*8.7+UP*8.7,stroke_width=20)
        L6=Line(RIGHT*8.7+UP*8.7,LEFT*8.7+DOWN*8.7,stroke_width=20)
        L1.set_color(YELLOW)
        L2.set_color(YELLOW)
        L3.set_color(YELLOW)
        L4.set_color(YELLOW)
        L5.set_color(YELLOW)
        L6.set_color(YELLOW)

        x=[]
        y=[]
        for i in range(len(r)):
            r[i]=r[i]+3
            x.append(r[i]*np.cos(j[i]/10))
            y.append(r[i]*np.sin(j[i]/10))
        d1=[]    
        d2=[]
        d3=[]    
        d4=[]       
        d5=[]    
        d6=[]      
        d7=[]    
        d8=[]      
        d9=[]   
        for i in range(1,len(r)):
            p1=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])
            p2=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])  
            p3=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])   
            p4=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])   
            p5=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])    
            p6=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])   
            p7=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])   
            p8=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i]) 
            p9=Line(UP*y[i-1]+RIGHT*x[i-1],UP*y[i]+RIGHT*x[i])
            p2.rotate(PI*17.5/180,about_point=[0,0,0])
            p4.rotate(PI*17.5/180,about_point=[0,0,0])
            p6.rotate(PI*17.5/180,about_point=[0,0,0])
            p8.rotate(PI*17.5/180,about_point=[0,0,0])
            
            p2.shift(RIGHT*8.6)         
            p3.shift(RIGHT*8.6+UP*8.6)     
            p4.shift(UP*8.6)         
            p5.shift(UP*8.6+LEFT*8.6)        
            p6.shift(LEFT*8.6)
            p7.shift(LEFT*8.6+DOWN*8.6)        
            p8.shift(DOWN*8.6)         
            p9.shift(RIGHT*8.6+DOWN*8.6)
            d1.append(p1)  
            d2.append(p2)  
            d3.append(p3)  
            d4.append(p4)  
            d5.append(p5)  
            d6.append(p6)  
            d7.append(p7)  
            d8.append(p8)  
            d9.append(p9)  
        for i in c:
            self.play(FadeIn(i))
        for i in d1:
            self.play(FadeIn(i))
        for i in d2:
            self.play(FadeIn(i))            
        for i in d3:
            self.play(FadeIn(i))  
        for i in d4:
            self.play(FadeIn(i))   
        for i in d5:
            self.play(FadeIn(i))   
        for i in d6:
            self.play(FadeIn(i))    
        for i in d7:
            self.play(FadeIn(i))   
        for i in d8:
            self.play(FadeIn(i))   
        for i in d9:
            self.play(FadeIn(i))   
        self.play(FadeIn(L1),FadeIn(L2),FadeIn(L3),FadeIn(L4),FadeIn(L5),FadeIn(L6))   
        for p in range(3600):
            for i in d1:
                i.rotate(PI/180,about_point=[0,0,0])
            for i in d2:
                i.rotate(-PI/180,about_point=[8.6,0,0])
            for i in d3:
                i.rotate(PI/180,about_point=[8.6,8.6,0])
            for i in d4:
                i.rotate(-PI/180,about_point=[0,8.6,0])
            for i in d5:
                i.rotate(PI/180,about_point=[-8.6,8.6,0])
            for i in d6:
                i.rotate(-PI/180,about_point=[-8.6,0,0])
            for i in d7:
                i.rotate(PI/180,about_point=[-8.6,-8.6,0])
            for i in d8:
                i.rotate(-PI/180,about_point=[0,-8.6,0])
            for i in d9:
                i.rotate(PI/180,about_point=[8.6,-8.6,0])
            self.wait(1)
            if p%20==0:
                print(p)
class dd(Scene):
    def construct(self):
        p=Line(UP+RIGHT,UP-RIGHT)
        self.play(FadeIn(p))        
        
        
        p.rotate(PI/4,about_point=[0,-3,0])
        
        
        
        
        self.wait(3)
        
        
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:12:27 2020

@author: admin


cd /d E:
cd E:\Strict\manim-master
python manim.py snake.py -pl
"""

import numpy as np
import random
from manimlib.imports import *
class tree(Scene):
    def construct(self):
        nn=np.zeros([322,322])       
        nexts=np.zeros([322,322])
        m=[]
        for i in range(1,41):
            for j in range(1,41):
                if random.randint(1,100)>66:
                    nn[i][j]=1
                s=Square(color=WHITE,fill_color=WHITE,fill_opacity=1)
                s.scale(0.5)
                s.move_to(UP*(i-20)+RIGHT*(j-20))
                m.append(s)
        self.Print(nn, m)
        for i in range(1):
            self.general(nn, nexts, m)
        
    def Print(self,nn,m):
        self.clear()
        print(len(m))
        for i in range(1,41):
            for j in range(1,41):
                if nn[i][j]==1:
                    self.play(FadeIn(m[(i-1)*20+j-1]))
        self.wait(2)
        
    def born(self,x,y,nn):
        n = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (i != 0 or j != 0):
                    if nn[x + i][y + j] == 1:
                        n+=1
        return n
    def general(self,nn,nexts,m):
        nt=0
        for i in range(1,41):
            for j in range(1,41):
                nt = self.born(j, i,nn);
                if nn[j][i] == 0:
                    if (nt == 3):
                        self.play(FadeIn(m[(i-1)*20+j-1]))
                        nexts[j][i] = 1
                    else:
                        nexts[j][i] = 0
                else:
                    if nt < 2 or nt>3:
                        self.play(FadeOut(m[(i-1)*20+j-1]))
                        nexts[j][i] = 0;
                    else:
                        nexts[j][i] = 1;
        for i in range(1,41):
            for j in range(1,41):
                nn[j][i] = nexts[j][i];
        
    


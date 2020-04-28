# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:44:44 2020


@author: 爱动脑的小王欣
"""

'''
        cd /d E:
cd E:\Strict\manim-master
python manim.py PythagoreanTree.py -pl
'''
import math
from manimlib.imports import *
class tree(Scene):
    def getDot(self,S,width,rota):
        P=S.get_center()

        A=Dot(P).copy().shift(width/2*UP+width/2*LEFT)
        B=Dot(P).copy().shift(width/2*UP+width/2*RIGHT)
        C=Dot(P).copy().shift(width/2*DOWN+width/2*RIGHT)
        D=Dot(P).copy().shift(width/2*DOWN+width/2*LEFT)
        '''self.play(ShowCreation(A))    
        self.play(ShowCreation(B))  
        self.play(ShowCreation(C))    
        self.play(ShowCreation(D))  '''
        A.rotate(rota,about_point=P)
        B.rotate(rota,about_point=P)
        C.rotate(rota,about_point=P)
        D.rotate(rota,about_point=P)

        return A.get_center(),B.get_center(),C.get_center(),D.get_center()
    
    def die(self,root,i,j):

        if i<0.2:
            return
        print(i) 
        A,B,C,D=self.getDot(root,i,j)
        S1=root.copy()      
        self.play(ShowCreation(S1))
        self.play(S1.rotate,PI-math.acos(3/5),{"about_point":A})
        self.play(S1.scale,4/5,{"about_point":A})
        self.die(S1,4/5*i,j+math.acos(4/5))
        S2=root.copy()
        self.play(ShowCreation(S2))
        self.play(S2.rotate,PI+math.acos(4/5),{"about_point":B})
        self.play(S2.scale,3/5,{"about_point":B})  
        self.die(S2,3/5*i,j-math.acos(3/5))

    def construct(self):
        S=Square(set_color=YELLOW,fill_color=YELLOW,fill_opacity=0.5)
        S.to_edge(DOWN)
        S.scale(1.5)
        width=S.get_width()
        self.play(ShowCreation(S))  
        self.die(S,width,0)

        

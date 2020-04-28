# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:40:38 2020

@author: admin
"""


'''
        cd /d E:
cd E:\Strict\manim-master
python manim.py Tangram.py -pl
'''
from manimlib.imports import *
import numpy as np
class Tangram(Scene):
    def construct(self):
        text1=TextMobject("答案呢，先不说，各位先思考下，（5秒钟暂停）")
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))
        time=['5','4','3','2','1']
        for i in time:
            text2=TextMobject(i)
            text2.scale(4)
            self.play(Write(text2))
            self.wait(1)
            self.play(FadeOut(text2))  
        self.wait(1)
        self.clear()

        a=Polygon(np.array([0,0,0]),np.array([4,0,0]),np.array([6,2,0]),np.array([2,2,0]),fill_color='#43CD80',fill_opacity=0.8)
        b=Polygon(np.array([0,0,0]),np.array([2,2,0]),np.array([-2,2,0]),np.array([-2,-2,0]),fill_color='#0000FF',fill_opacity=0.8)
        c=Polygon(np.array([0,0,0]),np.array([2,-2,0]),np.array([0,-4,0]),np.array([-2,-2,0]),fill_color='#FFEC8B',fill_opacity=0.8)
        d=Polygon(np.array([0,0,0]),np.array([2,-2,0]),np.array([4,0,0]),np.array([4,0,0]),fill_color='#FFB90F',fill_opacity=0.8)
        e=Polygon(np.array([2,-2,0]),np.array([6,2,0]),np.array([6,-2,0]),np.array([6,-6,0]),fill_color='#EE6363',fill_opacity=0.8)
        f=Polygon(np.array([2,-2,0]),np.array([6,-6,0]),np.array([2,-6,0]),np.array([-2,-6,0]),fill_color='#FF00FF',fill_opacity=0.8)
        g=Polygon(np.array([-2,-2,0]),np.array([-2,-4,0]),np.array([-2,-6,0]),np.array([0,-4,0]),fill_color='#FFE1FF',fill_opacity=0.8)


        p1=Polygon(np.array([-2,4,0]),np.array([0,4,0]),np.array([-1,3,0]),np.array([-2,2,0]),fill_color=RED,fill_opacity=0.3)
        p2=Polygon(np.array([2.828,4,0]),np.array([5.7,4,0]),np.array([5.7,1.172,0]),np.array([2.828,1.172,0]),fill_color=RED,fill_opacity=0.3)
        p3=Polygon(np.array([0,0,0]),np.array([0,1.172,0]),np.array([0,1.172,0]),np.array([0.6,0.572,0]),fill_color=RED,fill_opacity=0.3)

        self.play(ShowCreation(a))#平行四边形
        self.play(ShowCreation(b))#中等三角
        self.play(ShowCreation(c))#矩形
        self.play(ShowCreation(d))#小三角1
        self.play(ShowCreation(e))#大三角1
        self.play(ShowCreation(f))#大三角2
        self.play(ShowCreation(g))#中等三级
        self.play(ApplyMethod(e.rotate,-PI*9/2,{"about_point":np.array([6,2,0])}))
        self.play(ApplyMethod(e.shift,UP*2),run_Time=0.5)
        self.play(ApplyMethod(b.shift,RIGHT*7.7),run_Time=0.5)
        self.play(ApplyMethod(b.shift,UP*2),run_Time=0.5)
        self.play(ApplyMethod(g.rotate,PI/4,{"about_point":np.array([-2,-2,0])}))
        self.play(ApplyMethod(g.shift,LEFT*2.828),run_Time=0.5)
        self.play(ApplyMethod(g.shift,UP*6),run_Time=0.5)
        a2=Polygon(np.array([0,2,0]),np.array([4,2,0]),np.array([6,0,0]),np.array([2,0,0]),fill_color='#43CD80',fill_opacity=0.8)
        self.play(ReplacementTransform(a,a2))
        self.play(ApplyMethod(a2.rotate,-PI/2,{"about_point":np.array([0,2,0])}))
        self.play(ApplyMethod(a2.shift,UP*2),run_Time=0.5)

        self.play(ApplyMethod(c.rotate,PI/4,{"about_point":np.array([0,0,0])}))
        self.play(ApplyMethod(c.shift,UP*4),run_Time=0.5)

        self.play(ApplyMethod(f.rotate,-PI/4,{"about_point":np.array([6,-6,0])}))
        self.play(ApplyMethod(f.shift,UP*1.516+LEFT*0.3),run_Time=0.5)
        self.play(ApplyMethod(d.rotate,PI,{"about_point":np.array([2,-2,0])}))
        self.play(ApplyMethod(d.shift,LEFT*1.333),run_Time=0.5)
        self.play(ApplyMethod(d.shift,UP*2.586),run_Time=0.5)

        
        self.wait(2)
        self.play(FadeIn(p1),FadeIn(p2),FadeIn(p3),run_time=0.4)       
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3),run_time=0.2)   
        self.play(FadeIn(p1),FadeIn(p2),FadeIn(p3),run_time=0.4)       
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3),run_time=0.2)   
        self.play(FadeIn(p1),FadeIn(p2),FadeIn(p3),run_time=0.4)       
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3),run_time=0.2)   
        self.play(FadeIn(p1),FadeIn(p2),FadeIn(p3),run_time=0.4)       
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3),run_time=0.2)   
        self.play(FadeIn(p1),FadeIn(p2),FadeIn(p3),run_time=0.4)       
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3),run_time=0.2)   
        self.play(FadeIn(p1),FadeIn(p2),FadeIn(p3),run_time=0.4)       
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3),run_time=0.2)   
        self.play(FadeIn(p1),FadeIn(p2),FadeIn(p3),run_time=0.4)       
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3),run_time=0.2)   
        self.wait(2)
        
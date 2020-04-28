# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 00:19:01 2020

@author: 爱动脑的小王欣
"""

import math
import random
class gou(Scene):
    def construct(self):
        text1=TextMobject("大家好，我是小王欣")
        text2=TextMobject("疫情之下，各位是不是都闷在家里，无法出门，是不是很想看到森林美景")
        text3=TextMobject("那么我们今天就来试试用manim,来完成一棵树的建模")
        text4=TextMobject("喜欢可以刷个三连")
        self.play(Write(text1))
        self.play(ReplacementTransform(text1,text2))
        self.play(ReplacementTransform(text2,text3))
        self.play(ReplacementTransform(text3,text4))
        self.play(FadeOut(text4))
        L=Line(DOWN*7+LEFT*6,DOWN*7+RIGHT*6)
        self.play(FadeIn(L))
        self.tree(4.5,DOWN*7,0,15)
        self.tree(4.5,DOWN*7+DOWN*(random.random()*2-1)/2+LEFT*2,0,25)

        

        


    def tree(self,length,location,t,width):
        if length<0.3:
            for i in range(random.randint(20,100)):
                c=Circle()
                c.set_fill(PINK,opacity=1)
                c.set_color(PINK)
                c.move_to(location+(random.random()*UP+random.random()*DOWN+random.random()*RIGHT+random.random()*LEFT)/1.4)
                c.scale(0.3)
                self.play(FadeIn(c))
                print()
                return

        print(length)
        T1 = math.radians(t)
        p=location+length*math.cos(T1)*UP+length*math.sin(T1)*LEFT
        L=Line(location,p,stroke_width=width)
        L.set_color(LIGHT_BROWN)
        self.play(FadeIn(L));
        '''
        for i in range(random.randint(15,50)):
            c=Circle()
            c.set_fill(GREEN,opacity=1)
            c.set_color(GREEN)
            c.move_to(p+(random.random()*UP+random.random()*DOWN+random.random()*RIGHT+random.random()*LEFT)/3)
            c.scale(0.2)
            self.play(FadeIn(c))
        '''
        #d=Dot(p)
        self.tree(length*(0.24*random.random()+0.55),p,t+5+(30*random.random()),width*(random.random()*0.3+0.6))
        self.wait()
        self.tree(length*(0.24*random.random()+0.55),p,t-5-(30*random.random()),width*(random.random()*0.3+0.6))




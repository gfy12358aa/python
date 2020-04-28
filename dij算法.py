# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:35 2020

@author: 爱动脑的小王欣
"""


from manimlib.imports import *
from manimlib.utils import space_ops
class bao(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        t1=TextMobject("A","B","P","O")#"M","N")
        t1.set_color(BLACK)
        circle = Circle(radius = 2, color = DARK_BLUE, plot_depth=3)
        t1[3].move_to(DOWN*0.1+RIGHT*0.2)
        A=Dot(np.array([0, 2, 0]), color = RED)
        B=Dot(np.array([0, -2, 0]), color = RED)
        t1[0].next_to(A,UP,buff=0.3)    
        t1[1].next_to(B,UP,buff=0.3)
        P=Dot(color=BLUE, radius=0.07, plot_depth=4)
        t1[2].next_to(P,UP,buff=0.3)
        alpha = ValueTracker(0.0001)
        P.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())))
        t1[2].add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())+UP*0.3))
        line1=Line(A.get_center(),P.get_center(),stroke_width=3,color = RED)
        line2=Line(B.get_center(),P.get_center(),stroke_width=3,color = RED)
        line3=Line(np.array([-6,2,0]),np.array([6,2,0]),stroke_width=3,color = RED)
        line4=Line(np.array([-6,-2,0]),np.array([6,-2,0]),stroke_width=3,color = RED)
        line1.add_updater(lambda m: m.put_start_and_end_on(A.get_center(), A.get_center()+(P.get_center()-A.get_center())*3))
        line2.add_updater(lambda m: m.put_start_and_end_on(B.get_center(),B.get_center()+(P.get_center()-B.get_center())*3))

        self.play(ShowCreation(t1[3]),ShowCreation(circle))

        self.play(ShowCreation(t1[0]),ShowCreation(t1[1]),ShowCreation(A),ShowCreation(B))
        self.play(ShowCreation(line3),ShowCreation(line4),ShowCreation(line1),ShowCreation(line2),ShowCreation(P),ShowCreation(t1[2]))


        D1=Dot(line_intersection(line1.get_start_and_end(),line4.get_start_and_end()),color=YELLOW)
        D2=Dot(line_intersection(line2.get_start_and_end(),line3.get_start_and_end()),color=YELLOW)
        #t1[3].next_to(D1,UP,buff=0.3)
        #t1[4].next_to(D2,UP,buff=0.3)
        #self.play(ShowCreation(D1),ShowCreation(D2,set_opacity=0.2))
        L5=Line(D1,D2,stroke_width=3,color = GREEN)
        L5.add_updater(lambda m: m.put_start_and_end_on(Dot(line_intersection(line1.get_start_and_end(),line4.get_start_and_end()),color=YELLOW).get_center(),Dot(line_intersection(line2.get_start_and_end(),line3.get_start_and_end()),color=YELLOW).get_center()))
        trace = VGroup()
        self.i = 0
        def update_trace(m):
            self.i += 1
            m.add(L5.copy().clear_updaters())     
        self.play(ShowCreation(L5))
        self.add(trace)
        self.wait(2)
        trace.add_updater(update_trace)
        self.play(alpha.increment_value, 1, run_time=4, rate_func=linear)
        self.wait(5)

from manimlib.imports import *

class Homework_03(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        circle = Circle(radius = 3, color = DARK_BLUE, plot_depth=3).flip()
        center = Dot(color=GREEN)
        A = Dot(np.array([-2, 0, 0]), color = RED)
        alpha = ValueTracker(0.0001)
        B = Dot(color=BLUE, radius=0.7, plot_depth=4)
        B.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())))
        line1 = DashedLine(A.get_center(), B.get_center(), color=DARK_BROWN)
        line1.add_updater(lambda m: m.put_start_and_end_on(A.get_center(), B.get_center()))
        C = Dot(color=BLUE, radius=0.07, plot_depth=4)
        C.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())).flip(axis=B.get_center()-A.get_center(), about_point=ORIGIN))
        line2 = Line(B.get_center(), C.get_center(), color=ORANGE, stroke_width=3)
        line2.add_updater(lambda m: m.put_start_and_end_on(B.get_center(), C.get_center()))

        trace = VGroup()
        self.i = 0
        def update_trace(m):
            self.i += 1
            if self.i % 4 == 0:
                m.add(line2.copy().clear_updaters())

        self.wait(3)
        self.play(ShowCreation(circle), ShowCreation(center))
        self.wait()
        self.play(ShowCreation(A))
        alpha.set_value(0.2)
        self.play(ShowCreation(B))
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.6, run_time=1.6)
        self.play(ShowCreation(line1))
        self.wait()
        self.play(ShowCreation(C), ShowCreation(line2))
        self.wait(2)
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.7999, run_time=2, rate_func=linear)
        self.wait()
        self.add(trace)
        line2.set_stroke(width=2)
        self.wait(2)
        trace.add_updater(update_trace)
        alpha.set_value(0)
        anim = ApplyMethod(alpha.increment_value, 1, run_time=8, rate_func=linear)
        self.play(anim)
        self.wait(2)

        ellipse = Ellipse(width=6, height=2*np.sqrt(5), color=GREEN, plot_depth=10, run_time=2.5)
        self.play(ShowCreationThenDestruction(ellipse))
        self.wait(5)





class dij(Scene):
    def construct(self):
        '''
        cd /d E:
cd E:\Strict\manim-master
python manim.py dij算法.py -pl
        '''
        cir=[]
        ID=TextMobject("S","A","B","C","D","E","F","G","H")
        for i in range(9):
            c=Circle(color=WHITE)
            cir.append(c)
        cir[0].shift(np.array([-6,0,0]))
        cir[1].shift(np.array([-4,4,0]))
        cir[2].shift(np.array([0,4,0]))
        cir[3].shift(np.array([4,4,0]))
        cir[4].shift(np.array([8,0,0]))
        cir[5].shift(np.array([4,-4,0]))
        cir[6].shift(np.array([0,-4,0]))
        cir[7].shift(np.array([-4,-4,0]))
        cir[8].shift(np.array([-2,0,0]))
        for i in range(9):
            ID[i].next_to(cir[i],UP,buff=0.1)
            ID[i].scale(2)
        DIR=TextMobject("4","8","8","11","7","4","2","9","14","10","2","1","6","7")
        Line12=Line(np.array([-6,0,0]),np.array([-4,4,0]))
        Line18=Line(np.array([-6,0,0]),np.array([-4,-4,0]))
        Line23=Line(np.array([-4,4,0]),np.array([0,4,0]))
        Line28=Line(np.array([-4,4,0]),np.array([-4,-4,0]))
        Line34=Line(np.array([0,4,0]),np.array([4,4,0]))
        Line37=Line(np.array([0,4,0]),np.array([0,-4,0]))
        Line39=Line(np.array([0,4,0]),np.array([-2,0,0]))
        Line45=Line(np.array([4,4,0]),np.array([8,0,0]))
        Line46=Line(np.array([4,4,0]),np.array([4,-4,0]))
        Line56=Line(np.array([8,0,0]),np.array([4,-4,0]))
        Line67=Line(np.array([4,-4,0]),np.array([0,-4,0]))
        Line78=Line(np.array([0,-4,0]),np.array([-4,-4,0]))
        Line79=Line(np.array([0,-4,0]),np.array([-2,0,0]))
        Line89=Line(np.array([-4,-4,0]),np.array([-2,0,0]))
        DIR[0].move_to(UP*2+LEFT*5)
        DIR[1].move_to(DOWN*2+LEFT*5)
        DIR[2].move_to(UP*4+LEFT*2)
        DIR[3].move_to(UP*0+LEFT*4)
        DIR[4].move_to(UP*4+RIGHT*2)
        DIR[5].move_to(UP*3+LEFT*1)
        DIR[6].move_to(UP*2+RIGHT*6)
        DIR[7].move_to(RIGHT*4)
        DIR[8].move_to(DOWN*2+RIGHT*6)
        DIR[9].move_to(DOWN*4+RIGHT*2)
        DIR[10].move_to(DOWN*4+LEFT*2)
        DIR[11].move_to(DOWN*3+LEFT*1)
        DIR[12].move_to(DOWN*3+LEFT*3)
        DIR[13].move_to(RIGHT*0)


        for i in cir:
            #DIR[i].set_color=RED_A
            self.play(FadeIn(i))
        self.play(FadeIn(Line12))
        self.play(FadeIn(Line18))
        self.play(FadeIn(Line23))
        self.play(FadeIn(Line28))
        self.play(FadeIn(Line34))
        self.play(FadeIn(Line37))
        self.play(FadeIn(Line39))
        self.play(FadeIn(Line45))
        self.play(FadeIn(Line46))
        self.play(FadeIn(Line56))
        self.play(FadeIn(Line67))
        self.play(FadeIn(Line78))
        self.play(FadeIn(Line79))
        self.play(FadeIn(Line89))
        for i in DIR:
            i.scale(1.5)
            self.play(Write(i))
        for i in ID:
            self.play(Write(i))

        text6=TextMobject("dijstras算法")
        text6.move_to(UP*7+LEFT*9)
        text6.scale(2)
        L=Line(np.array([-8,8,0]),np.array([8,8,0]))
        L.next_to(text6,DOWN,buff=0.5)
        

        self.play(FadeIn(L),Write(text6))
        node0=TextMobject("0")
        node1=TextMobject("4 S","")
        node2=TextMobject("12 SA","")
        node3=TextMobject("19 SAB","")
        node4=TextMobject("21 SABC","")
        node5=TextMobject("20 SGF","")
        node6=TextMobject("10 SG","")
        node7=TextMobject("8 S","0","")
        node8=TextMobject("14 SG","11 SGF")
        for i in node0:
            i.next_to(cir[0],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node1:
            i.next_to(cir[1],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node2:
            i.next_to(cir[2],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node3:
            i.next_to(cir[3],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node4:
            i.next_to(cir[4],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node5:
            i.next_to(cir[5],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node6:
            i.next_to(cir[6],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node7:
            i.next_to(cir[7],DOWN,buff=0.7)
            i.set_color(BLUE)
        for i in node8:
            i.next_to(cir[8],DOWN,buff=0.7)
            i.set_color(BLUE)
        self.play(FadeIn(node0))
        
        cir[0].set_color(YELLOW)
        cir[0].set_fill(YELLOW,opacity=0.4)
        self.play(ApplyMethod(Line12.set_color,PINK),ApplyMethod(Line18.set_color,PINK))
        self.play(ApplyMethod(Line12.set_color,WHITE),ApplyMethod(Line18.set_color,WHITE))
        self.wait(1)

        self.play(FadeIn(node1[0]),FadeIn(node7[0]))
        self.wait(1)
        
        cir[1].set_color(YELLOW)
        cir[1].set_fill(YELLOW,opacity=0.4)
        self.play(ApplyMethod(Line23.set_color,PINK),ApplyMethod(Line28.set_color,PINK))
        self.play(ApplyMethod(Line23.set_color,WHITE),ApplyMethod(Line28.set_color,WHITE))
        self.wait(1)
        self.play(FadeIn(node2[0]))
        self.wait(1)
        

        cir[7].set_color(YELLOW)
        cir[7].set_fill(YELLOW,opacity=0.4)
        self.play(ApplyMethod(Line78.set_color,PINK),ApplyMethod(Line89.set_color,PINK))
        self.play(ApplyMethod(Line78.set_color,WHITE),ApplyMethod(Line89.set_color,WHITE))
        self.wait(1)
        self.play(FadeIn(node6[0]),FadeIn(node8[0]))
        self.wait(1)        
        
        
        cir[6].set_color(YELLOW)
        cir[6].set_fill(YELLOW,opacity=0.4)
        self.play(ApplyMethod(Line79.set_color,PINK),ApplyMethod(Line37.set_color,PINK),ApplyMethod(Line67.set_color,PINK))
        self.play(ApplyMethod(Line79.set_color,WHITE),ApplyMethod(Line37.set_color,WHITE),ApplyMethod(Line67.set_color,WHITE))
        self.wait(1)
        self.play(FadeOut(node8[0]),FadeIn(node8[1]),FadeIn(node5[0]),FadeIn(node8[0]))
        self.wait(1)  
        
        
        cir[8].set_color(YELLOW)
        cir[8].set_fill(YELLOW,opacity=0.4)
        self.play(ApplyMethod(Line39.set_color,PINK))
        self.play(ApplyMethod(Line39.set_color,WHITE))
        self.wait(1)

        cir[2].set_color(YELLOW)
        cir[2].set_fill(YELLOW,opacity=0.4)
        self.play(ApplyMethod(Line34.set_color,PINK))
        self.play(ApplyMethod(Line34.set_color,WHITE))
        self.wait(1)
        self.play(FadeIn(node3[0]))
        self.wait(1)       
        
        
        
        
        cir[3].set_color(YELLOW)
        cir[3].set_fill(YELLOW,opacity=0.4)
        self.play(ApplyMethod(Line45.set_color,PINK),ApplyMethod(Line46.set_color,PINK))
        self.play(ApplyMethod(Line45.set_color,WHITE),ApplyMethod(Line46.set_color,WHITE))
        self.wait(1)
        self.play(FadeIn(node4[0]))
        self.wait(1)     
        
        
        cir[5].set_color(YELLOW)
        cir[5].set_fill(YELLOW,opacity=0.4)
        self.wait(1)  

        cir[4].set_color(YELLOW)
        cir[4].set_fill(YELLOW,opacity=0.4)
        self.wait(1)
        self.play(FadeIn(node4[0]))
        self.wait(1)             
        
        
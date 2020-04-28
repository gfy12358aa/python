# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:46:01 2020

@author: admin
"""

from manimlib.imports import *
import  queue
import numpy as np
import time
class snake(Scene):
    def construct(self):
        #Screen=Rectangle(color=YELLOW,fill_color=YELLOW,fill_opacity=0.2,width=8,height=8)
        title=TextMobject("python 贪吃蛇")
        title.to_edge(UP)
        self.play(Write(title))

        self.get_start_info()               #欢迎信息
        self.running_game(snake_speed=2)
        self.show_gameover_info()
    def isIn(self,snake_coords,x1,y1):
        for coord in snake_coords:
            if coord['x']==x1 and coord['y']==y1:
                return False
        return True
        
    #游戏主体
    def running_game(self,snake_speed):
        startx = random.randint(3, 5) #开始位置
        starty = random.randint(3, 5)
        snake_coords = [{'x': startx, 'y': starty},  #初始贪吃蛇
                        {'x': startx - 1, 'y': starty},
                        {'x': startx - 2, 'y': starty}]
        snakee=[]           
        '''
        cd /d E:
cd E:\Strict\manim-master
python manim.py snake.py -pl
        '''
        Screen=Rectangle(color=YELLOW,fill_color=YELLOW,fill_opacity=0.2,width=10,height=10)
        Screen.shift(UP+RIGHT)
        title=TextMobject("python 贪吃蛇")
        title.to_edge(UP)
        self.play(FadeIn(Screen),Write(title))
        
        c=[]
        for i in range(3):
            s = Square(color=GREEN,fill_color=GREEN,fill_opacity=1)
            s.move_to(UP*(snake_coords[i]['x']-3)+RIGHT*(snake_coords[i]['y']-3))
            s.scale(0.5)
            snakee.append(s)
            self.play(FadeIn(s),run_time=0.1)
        direction = RIGHT       #  开始时向右移动   
        f=[]
        food={}
        sss=[]
        x1=0
        y1=0
        while True:     
            x1=random.randint(1, 7)
            y1=random.randint(1, 7) # 实物位置重新设置
            if self.isIn(snake_coords,x1,y1)==False:
                continue
            #print(x1,y1)
            food['x'] =x1
            food['y'] =y1
            break
        self.draw_food(food,f)    
        i=0
        while i<6:
            i+=1
            print(i)
            self.snake_is_eat(snake_coords, food,snakee,f) #判断蛇是否吃到食物
            self.direction = self.get_directe(snake_coords,food)
            if np.all(self.direction==[0,0,0]):
                break

            self.move_snake(self.direction, snake_coords,snakee) #移动蛇
        
            ret = self.snake_is_alive(snake_coords)
            if not ret:
                break #蛇跪了. 游戏结束

            
            #self.draw_snake(snake_coords,snakee)

            self.draw_score(len(snake_coords) - 3,sss)
            self.wait(snake_speed)




    def draw_food(self,food,f):

        apple=Circle(fill_color=RED,fill_opacity=1)
        apple.scale(0.5)
        apple.move_to(UP*(food['x']-3)+RIGHT*(food['y']-3))
        f.append(apple)
        self.play(FadeIn(apple))
    
    
    
    #def draw_snake(self,snake_coords):
        # coord in snake_coords:
            #x = coord['x']-3
            #y = coord['y']-3
            #snake_squ = Square(color=GREEN,fill_color=GREEN,fill_opacity=1)
            #snake_squ.move_to(UP*y+RIGHT*x)
            #snake_squ.scale(00.5)
            #self.play(FadeIn(snake_squ))

    def move_snake(self,direction,snake_coords,snakee):

        if  np.all(direction == RIGHT):
            newHead = {'x': snake_coords[0]['x'] + 1, 'y': snake_coords[0]['y']}
        elif np.all(direction == LEFT):
            newHead = {'x': snake_coords[0]['x'] - 1, 'y': snake_coords[0]['y']}
        elif np.all(direction == DOWN):
            newHead = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] - 1}
        else:#
            newHead = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] + 1}
            
            
            
        snake_coords.insert(0, newHead)
        ss = Square(color=GREEN,fill_color=GREEN,fill_opacity=1)
        ss.move_to(UP*(newHead['x']-3)+RIGHT*(newHead['y']-3))
        ss.scale(00.5)
        self.play(FadeIn(ss))

        snakee.insert(0,ss)
        return 0

    def snake_is_alive(self,snake_coords):
        tag = True
        if snake_coords[0]['x'] == -1 or snake_coords[0]['x'] == 8 or snake_coords[0]['y'] == -1 or  snake_coords[0]['y'] == 8:
            tag = False # 蛇碰壁啦
        for snake_body in snake_coords[1:]:
            if snake_body['x'] == snake_coords[0]['x'] and snake_body['y'] == snake_coords[0]['y']:
                tag = False # 蛇碰到自己身体啦
        return tag


    def bfs(self,maze,x1,y1,x2,y2):
        n, m = len(maze), len(maze[0])
        dist = [[999 for _ in range(m)] for _ in range(n)]
        pre = [[None for _ in range(m)] for _ in range(n)]   # 当前点的上一个点,用于输出路径轨迹

 
        dx = [1, 0, -1, 0] # 四个方位
        dy = [0, 1, 0, -1]
        sx, sy =x1,y1
        gx, gy = x2, y2
 
        dist[sx][sy] = 0
        q = queue.Queue()
        q.put([x1,y1])      
        find = False
        while q.empty()!=True:
            curr = q.get()

            for i in range(4):
                nx, ny = curr[0] + dx[i], curr[1] + dy[i]
                if 0<=nx<n and 0<=ny<m and maze[nx][ny] != 1 and dist[nx][ny] == 999:
                    dist[nx][ny] = dist[curr[0]][curr[1]] + 1
                    pre[nx][ny] = curr
                    q.put([nx, ny])
                    if nx == gx and ny == gy:
                        find = True
                        break
                    if find:
                        break
        if find==False:
            return [-1]
        stack = []
        curr = [x2,y2]
        while True:
            stack.append(curr)
            if curr[0] == x1 and curr[1]== y1:
                break
            prev = pre[curr[0]][curr[1]]
            curr = prev
        x=0
        y=0
        x=stack[len(stack)-2][0]       
        y=stack[len(stack)-2][1]
        while len(stack)>0:
            curr = stack.pop()   
        return [x, y]
                

    def get_directe(self,snake_coords,food):
        m=np.zeros([8,8])
        for i in range(1,len(snake_coords)):
            m[snake_coords[i]['x']][snake_coords[i]['y']]=1
        m[food['x']][food['y']]=2
        x1=snake_coords[0]['x']
        y1=snake_coords[0]['y']
        x2=food['x']
        y2=food['y']
        p=self.bfs(m,x1,y1,x2,y2)
        #print(p)
        #不存在到达食物的路径
        if p[0]==-1:
            d=[UP,DOWN, RIGHT,LEFT]
            return d[random.randint(0,3)]
        else:
            if p[0]-x1==0:
                if p[1]-y1==1:
                    #print(UP)
                    return UP
                
                else:
                    #print(DOWN)
                    return DOWN
            elif p[1]-y1==0:
                if p[0]-x1==1:             
                    #print(RIGHT)
                    return RIGHT
                else:                   
                    #print(LEFT)
                    return LEFT



    def snake_is_eat(self,snake_coords,food,snakee,f):
        x2=food['x']
        y2=food['y']
        if snake_coords[0]['x'] == food['x'] and snake_coords[0]['y'] == food['y']:
            while True:
                self.play(FadeOut(f[0]))
                x1=random.randint(1, 7)
                y1=random.randint(1, 7) # 实物位置重新设置

                if self.isIn(snake_coords,x1,y1)==False:
                    continue
                food['x'] =x1
                food['y'] =y1
                del f[-1]
                self.draw_food(food,f)
                break
        else:
            del snake_coords[-1]  # 如果没有吃到实物, 就向前移动, 那么尾部一格删掉   
            self.play(FadeOut(snakee[-1]))
            del snakee[-1]
  

    def get_start_info(self):
        title=TextMobject("游戏即将开始，请稍后")
        title.scale(2)
        self.play(Write(title)) 
        self.wait(3)
        self.play(FadeOut(title))
    def show_gameover_info(self):
        return 0
    def draw_score(self,score,sss):
        if len(sss)>0:
            self.play(FadeOut(sss[0]))
            del sss[-1]
        scoreSurf = TextMobject('得分: %s' % score)
        scoreSurf.to_corner(UR)
        sss.append(scoreSurf)
        self.play(FadeIn(scoreSurf))
    def terminate(self):
        return 0
    
class snake20(Scene):
    def construct(self):
        #Screen=Rectangle(color=YELLOW,fill_color=YELLOW,fill_opacity=0.2,width=8,height=8)
        title=TextMobject("python 贪吃蛇")
        title.to_edge(UP)
        self.play(Write(title))

        self.get_start_info()               #欢迎信息
        self.running_game(snake_speed=2)
        self.show_gameover_info()
    def isIn(self,snake_coords,x1,y1):
        for coord in snake_coords:
            if coord['x']==x1 and coord['y']==y1:
                return False
        return True
        
    #游戏主体
    def running_game(self,snake_speed):
        startx = random.randint(3, 5) #开始位置
        starty = random.randint(3, 5)
        snake_coords = [{'x': startx, 'y': starty},  #初始贪吃蛇
                        {'x': startx - 1, 'y': starty},
                        {'x': startx - 2, 'y': starty},
                        {'x': startx - 3, 'y': starty}]
        snakee=[]           
        '''
        cd /d E:
cd E:\Strict\manim-master
python manim.py snake.py -pl
        '''
        Screen=Rectangle(color=YELLOW,fill_color=YELLOW,fill_opacity=0.2,width=9,height=9)
        Screen.move_to(UP*0.5+DOWN*0.5)
        title=TextMobject("python 贪吃蛇")
        title.to_edge(UP)
        self.play(FadeIn(Screen),Write(title))
        
        c=[]
        for i in range(3):
            s = Square(color=GREEN,fill_color=GREEN,fill_opacity=1)
            s.move_to(UP*(snake_coords[i]['x']-3)+RIGHT*(snake_coords[i]['y']-3))
            s.scale(0.4)
            snakee.append(s)
            self.play(FadeIn(s),run_time=0.1)
        direction = RIGHT       #  开始时向右移动   
        f=[]
        food={}
        sss=[]
        x1=0
        y1=0
        while True:     
            x1=random.randint(1, 7)
            y1=random.randint(1, 7) # 实物位置重新设置
            if self.isIn(snake_coords,x1,y1)==False:
                continue
            #print(x1,y1)
            food['x'] =x1
            food['y'] =y1
            break
        self.draw_food(food,f)    
        i=0
        while i<5000:
            i+=1
            print(i)

            print(snake_coords)

            self.direction = self.get_directe(snake_coords,food)
            if np.all(self.direction==[0,0,0]):
                print("无法前进")
                break
            print(snake_coords)

            self.move_snake(self.direction, snake_coords,snakee) #移动蛇
            self.snake_is_eat(snake_coords, food,snakee,f) #判断蛇是否吃到食物
            ret = self.snake_is_alive(snake_coords)
            if not ret:
                break #蛇跪了. 游戏结束

            
            #self.draw_snake(snake_coords,snakee)

            self.draw_score(len(snake_coords) - 3,sss)
            self.wait(snake_speed)




    def draw_food(self,food,f):

        apple=Circle(fill_color=RED,fill_opacity=1)
        apple.scale(0.4)
        apple.move_to(UP*(food['x']-3)+RIGHT*(food['y']-3))
        f.append(apple)
        self.play(FadeIn(apple))
    
    
    
    #def draw_snake(self,snake_coords):
        # coord in snake_coords:
            #x = coord['x']-3
            #y = coord['y']-3
            #snake_squ = Square(color=GREEN,fill_color=GREEN,fill_opacity=1)
            #snake_squ.move_to(UP*y+RIGHT*x)
            #snake_squ.scale(00.5)
            #self.play(FadeIn(snake_squ))

    def move_snake(self,direction,snake_coords,snakee):

        
        if  np.all(direction == RIGHT):
            newHead = {'x': snake_coords[0]['x'] + 1, 'y': snake_coords[0]['y']}
        elif np.all(direction == LEFT):
            newHead = {'x': snake_coords[0]['x'] - 1, 'y': snake_coords[0]['y']}
        elif np.all(direction == DOWN):
            newHead = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] - 1}
        else:#
            newHead = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] + 1}
            
            
            
        snake_coords.insert(0, newHead)
        ss = Square(color=GREEN,fill_color=GREEN,fill_opacity=1)
        ss.move_to(UP*(newHead['x']-3)+RIGHT*(newHead['y']-3))
        ss.scale(00.4)
        self.play(FadeIn(ss))

        snakee.insert(0,ss)
        return 0

    def snake_is_alive(self,snake_coords):
        tag = True
        if snake_coords[0]['x'] == -1 or snake_coords[0]['x'] == 8 or snake_coords[0]['y'] == -1 or  snake_coords[0]['y'] == 8:
            tag = False # 蛇碰壁啦
        for snake_body in snake_coords[1:]:
            if snake_body['x'] == snake_coords[0]['x'] and snake_body['y'] == snake_coords[0]['y']:
                tag = False # 蛇碰到自己身体啦
        return tag


    def bfs(self,maze,x1,y1,x2,y2):
        n, m = len(maze), len(maze[0])
        dist = [[999 for _ in range(m)] for _ in range(n)]
        pre = [[None for _ in range(m)] for _ in range(n)]   # 当前点的上一个点,用于输出路径轨迹
        

 
        dx = [1, 0, -1, 0] # 四个方位
        dy = [0, 1, 0, -1]
        sx, sy =x1,y1
        gx, gy = x2, y2
 
        dist[sx][sy] = 0
        q = queue.Queue()
        q.put([x1,y1])      
        find = False
        while q.empty()!=True:
            curr = q.get()

            for i in range(4):
                nx, ny = curr[0] + dx[i], curr[1] + dy[i]
                if 0<=nx<n and 0<=ny<m and maze[nx][ny] != 1 and dist[nx][ny] == 999:
                    dist[nx][ny] = dist[curr[0]][curr[1]] + 1
                    pre[nx][ny] = curr
                    q.put([nx, ny])
                    if nx == gx and ny == gy:
                        find = True
                        break
                    if find:
                        break
        if find==False:
            return [-1]
        stack = []
        curr = [x2,y2]
        while True:
            stack.append(curr)
            if curr[0] == x1 and curr[1]== y1:
                break
            prev = pre[curr[0]][curr[1]]
            curr = prev
        x=0
        y=0
        if len(stack)==1:
            return stack[0]
        x=stack[len(stack)-2][0]       
        y=stack[len(stack)-2][1]
        
        return [x, y]
                

        
    def vir_snake(self,snake_coords,food):
        sn=[]
        for j in snake_coords:
            sn.append(j)
        direction=[0,0,0]
        x1=sn[0]['x']
        y1=sn[0]['y']
        x2=food['x']
        y2=food['y']
        while True:
            x1=sn[0]['x']
            y1=sn[0]['y']
            x2=food['x']
            y2=food['y']   
            m=np.zeros([8,8])
            for i in range(len(sn)):
                m[sn[i]['x']][sn[i]['y']]=1
            m[food['x']][food['y']]=6
            r=self.bfs(m,x1,y1,x2,y2)
            if r[0]==-1:
                return [0,0,0]
            if r[0]-x1==0:
                if r[1]-y1==1:
                    direction=UP
                else:
                    direction=DOWN
            elif r[1]-y1==0:
                if r[0]-x1==1:
                    direction=RIGHT
                else:
                    direction=LEFT
            
            if  np.all(direction == RIGHT):
                newHead = {'x': sn[0]['x'] + 1, 'y': sn[0]['y']}
            elif np.all(direction == LEFT):
                newHead = {'x': sn[0]['x'] - 1, 'y': sn[0]['y']}
            elif np.all(direction == DOWN):
                newHead = {'x': sn[0]['x'], 'y': sn[0]['y'] - 1}
            else:#
                newHead = {'x': sn[0]['x'], 'y': sn[0]['y'] + 1}
            sn.insert(0, newHead)
            del sn[-1]
            
            
            if sn[0]['x']==x2 and sn[0]['y']==y2:
                break
        print("虚拟蛇")
        print(snake_coords)
        print(sn)
        print(food)
        mm=np.zeros([8,8])
        for i in range(len(sn)):
            mm[sn[i]['x']][sn[i]['y']]=1
        mm[sn[len(sn)-1]['x']][sn[len(sn)-1]['y']]=6
        x5=sn[0]['x']
        y5=sn[0]['y']
        x6=sn[len(sn)-1]['x']
        y6=sn[len(sn)-1]['y']
        pp=self.bfs(mm,x5,y5,x6,y6)

        if pp[0]!=-1:
            if pp[0]-x5==0:
                if pp[1]-y5==1:
                    return UP
                else:
                    return DOWN
            elif pp[1]-y5==0:
                if pp[0]-x5==1:
                    return RIGHT
                else:
                    return LEFT
        else:
            return [0,0,0]
            
    def get_d(self,snake_coords,food):    
        d=[0,0,0]
        maxlength=-1
        dirs=[UP,DOWN,LEFT,RIGHT]
        
        print(food)
        for p in range(len(dirs)):
            sn=[]
            sn.clear()
            for j in snake_coords:
                sn.append(j)

            if np.all(dirs[p] == RIGHT):
                newHead = {'x': sn[0]['x'] + 1, 'y': sn[0]['y']}
            elif  np.all(dirs[p]  == LEFT):
                newHead = {'x': sn[0]['x'] - 1, 'y': sn[0]['y']}
            elif  np.all(dirs[p]  == DOWN):
                newHead = {'x': sn[0]['x'], 'y': sn[0]['y'] - 1}
            elif np.all(dirs[p]  == UP):
                newHead = {'x': sn[0]['x'], 'y': sn[0]['y'] + 1}
            else:
                continue
            b=False
            for i in range(0,len(sn)-1):
                if newHead['x']==sn[i]['x'] and newHead['y']==sn[i]['y']:
                    b=True
                    break
            if b==True:
                continue

            if newHead['x']<0 or newHead['y']<0 or newHead['x']>=8 or  newHead['y']>=8:
                continue
            sn.insert(0, newHead)
            print(newHead)
            del sn[-1]
            mm=np.zeros([8,8])
            for i in range(len(sn)):
                mm[sn[i]['x']][sn[i]['y']]=1
            mm[sn[len(sn)-1]['x']][sn[len(sn)-1]['y']]=6
            x2=sn[len(sn)-1]['x']
            y2=sn[len(sn)-1]['y']
            x1=sn[0]['x']
            y1=sn[0]['y']
            q=self.bfs(mm,x1,y1,x2,y2) 
            if q[0]!=-1:
                length_apple=(x2-food['x'])*(x2-food['x'])+(y2-food['y'])*(y2-food['y'])
                print(length_apple)
                #print(length_apple)
                #print()
                if maxlength<length_apple:
                    maxlength=length_apple
                    d=dirs[p]
        print(snake_coords)
        return d
                
                          
    '''
    策略1：判断食物与尾巴之间是否存在路径
    '''    
    def get_directe(self,snake_coords,food):
        m=np.zeros([8,8])
        for i in range(len(snake_coords)):
            m[snake_coords[i]['x']][snake_coords[i]['y']]=1
        m[snake_coords[0]['x']][snake_coords[0]['y']]=4
        m[food['x']][food['y']]=6   

        #print(m)
        m[snake_coords[0]['x']][snake_coords[0]['y']]=1
        m[food['x']][food['y']]=0
        
        
        x1=snake_coords[len(snake_coords)-1]['x']
        y1=snake_coords[len(snake_coords)-1]['y']
        x2=food['x']
        y2=food['y']
        p=self.bfs(m,x1,y1,x2,y2)  

        #print(p)
        '''
        不存在尾巴到达食物的路径
        '''
        if p[0]==-1:
            x5=snake_coords[0]['x']
            y5=snake_coords[0]['y']
            x6=snake_coords[len(snake_coords)-1]['x']
            y6=snake_coords[len(snake_coords)-1]['y']
            for i in range(len(snake_coords)):
                m[snake_coords[i]['x']][snake_coords[i]['y']]=1
            m[snake_coords[len(snake_coords)-1]['x']][snake_coords[len(snake_coords)-1]['y']]=6  
            pp=self.bfs(m,x5,y5,x6,y6)
            print("尾巴到不了食物")
            if pp[0]==-1:
                print("自己看不见尾巴")
                dir=[UP,DOWN,RIGHT,LEFT]
                i=0
                while True:
                    u=dir[i]
                    i+=1
                    if snake_coords[0]['y']+ 1<8:
                        if(np.all(u==UP) and m[snake_coords[0]['x']][snake_coords[0]['y']+ 1]!=1):
                            return u
                    if snake_coords[0]['y']- 1>=0:
                        if(np.all(u==DOWN) and m[snake_coords[0]['x']][snake_coords[0]['y']- 1]!=1):
                            return u   
                    if snake_coords[0]['x']+ 1>=0:
                        if(np.all(u==LEFT) and m[snake_coords[0]['x']-1][snake_coords[0]['y']]!=1):
                            return u           
                    if snake_coords[0]['x']+ 1<8:
                        if(np.all(u==RIGHT) and m[snake_coords[0]['x'] + 1][snake_coords[0]['y']]!=1):
                            return u   
                    if i>3:
                        return [0,0,0]       
                                
            else:
                md=self.vir_snake(snake_coords,food)
                if(np.all(md==np.array([0,0,0]))):
                    print("追尾")
                    if pp[0]-x5==0:
                        if pp[1]-y5==1:
                            return UP
                        else:
                            return DOWN
                    elif pp[1]-y5==0:
                        if pp[0]-x5==1:
                            return RIGHT
                        else:
                            return LEFT
                else:
                    print("走一步")
                    return md
           
        #存在尾巴到达食物的路径（安全）
        else:
            print("安全路径")
            x3=snake_coords[0]['x']
            y3=snake_coords[0]['y']
            x4=food['x']
            y4=food['y']
                        
            for i in range(len(snake_coords)):
                m[snake_coords[i]['x']][snake_coords[i]['y']]=1
            #m[snake_coords[len(snake_coords)-1]['x']][snake_coords[len(snake_coords)-1]['y']]=6  
            m[food['x']][food['y']]=6 
            
            pp=self.bfs(m,x3,y3,x4,y4)
            #print(pp)
            if pp[0]==-1:
                print("看不见食物")

                x3=snake_coords[0]['x']
                y3=snake_coords[0]['y']
                x4=snake_coords[len(snake_coords)-1]['x']
                y4=snake_coords[len(snake_coords)-1]['y']
                for i in range(len(snake_coords)):
                    m[snake_coords[i]['x']][snake_coords[i]['y']]=1
                m[snake_coords[len(snake_coords)-1]['x']][snake_coords[len(snake_coords)-1]['y']]=6  

                ppp=self.bfs(m,x3,y3,x4,y4)
                #不存在到达尾巴的路径
                if ppp[0]==-1:
                    print("看不见尾巴")
                    return self.get_d(snake_coords,food)
                    
                    dir=[UP,DOWN,RIGHT,LEFT]     
                    i=0
                    while True:
                        u=dir[i]
                        i+=1
                        if snake_coords[0]['y']+ 1<8:
                            if(np.all(u==UP) and m[snake_coords[0]['x']][snake_coords[0]['y']+ 1]!=1):
                                return u
                        if snake_coords[0]['y']- 1>=0:
                            if(np.all(u==DOWN) and m[snake_coords[0]['x']][snake_coords[0]['y']- 1]!=1):
                                return u   
                        if snake_coords[0]['x']+ 1>=0:
                            if(np.all(u==LEFT) and m[snake_coords[0]['x']-1][snake_coords[0]['y']]!=1):
                                return u           
                        if snake_coords[0]['x']+ 1<8:
                            if(np.all(u==RIGHT) and m[snake_coords[0]['x'] + 1][snake_coords[0]['y']]!=1):
                                return u   
                        if i>3:
                            return [0,0,0]
                    
                else:
                    print("看见尾巴")
                    return self.get_d(snake_coords,food)
            else:
                print("看见食物")
                md=self.vir_snake(snake_coords,food)
                if(np.all(md==np.array([0,0,0]))):    
                    print("追尾")
                    return self.get_d(snake_coords,food)
                else:
                    print("走一步")
                    if pp[0]-x3==0:
                        if pp[1]-y3==1:
                            return UP
                        else:
                            return DOWN
                    elif pp[1]-y3==0:
                        if pp[0]-x3==1:
                            return RIGHT
                        else:
                            return LEFT



    def snake_is_eat(self,snake_coords,food,snakee,f):
        x2=food['x']
        y2=food['y']
        if snake_coords[0]['x'] == food['x'] and snake_coords[0]['y'] == food['y']:
            while True:
                self.play(FadeOut(f[0]))
                x1=random.randint(0,7)
                time.sleep(1)
                y1=random.randint(0, 7) # 实物位置重新设置
                time.sleep(1)
                if self.isIn(snake_coords,x1,y1)==False:
                    continue
                food['x'] =x1
                food['y'] =y1
                del f[-1]
                self.draw_food(food,f)
                break
        else:
            del snake_coords[-1]  # 如果没有吃到实物, 就向前移动, 那么尾部一格删掉   
            self.play(FadeOut(snakee[-1]))
            del snakee[-1]
  

    def get_start_info(self):
        title=TextMobject("游戏即将开始，请稍后")
        title.scale(2)
        self.play(Write(title)) 
        self.wait(3)
        self.play(FadeOut(title))
    def show_gameover_info(self):
        return 0
    def draw_score(self,score,sss):
        if len(sss)>0:
            self.play(FadeOut(sss[0]))
            del sss[-1]
        scoreSurf = TextMobject('得分: %s' % score)
        scoreSurf.to_corner(UR)
        sss.append(scoreSurf)
        self.play(FadeIn(scoreSurf))
    def terminate(self):
        return 0    
class Text(Scene):
    def construct(self):
        #Screen=Rectangle(color=YELLOW,fill_color=YELLOW,fill_opacity=0.2,width=8,height=8)
        title=TextMobject("MANIM","=？=","游戏引擎")
        title[0].set_color(YELLOW)
        title[1].set_color(PINK)
        title[2].set_color(YELLOW)
        title[0].rotate(PI/9)
        title[2].rotate(PI/9)
        self.play(Write(title))
        self.wait(3)
        '''
        text1=TextMobject("大家好")
        text2=TextMobject("大家可能都接触过贪吃蛇吧")
        text3=TextMobject("那想没想过自己亲自去编写一个ai来控制贪吃蛇呢")
        text4=TextMobject("今天，小王欣就来带领你，去一步步的编写贪吃蛇的ai")
        text5=TextMobject("简单版本")
        text6=TextMobject("我们先不去想蛇身过长的这个事实")
        text7=TextMobject("先将问题简化")
        text8=TextMobject("给你蛇头和一个食物，要避开障碍物(蛇身)")
        text82=TextMobject("从起点找到一条可行路到达终点")
        text9=TextMobject("我们可以用的方法有：BFS、DFS、A*")
        text10=TextMobject("这里我们采用BFS算法")
        text11=TextMobject("但蛇很容易就进入一个蛇身围起来封闭空间时会导致死亡")
        text12=TextMobject("那么我们有什么方法可以不让蛇挂掉呢")
        text13=TextMobject("等5秒钟","5","4","3","2","1")
        text14=TextMobject("好，相信大家都思考过了")
        text15=TextMobject("如果蛇吃完食物后仍存在一条到蛇尾安全路径，蛇去吃食物")
        text151=TextMobject("否则蛇继续追着蛇尾跑")
        text16=TextMobject("小伙伴们你们明白了吗")
        text17=TextMobject("喜欢记得关注我呀")
        text18=TextMobject("源码之后会上传GitHub或者百度云")

        text5.to_corner(UL)
        text6.to_edge(DOWN)
        text7.to_edge(DOWN)
        text8.to_edge(DOWN)
        text82.to_edge(DOWN)
        text9.to_edge(DOWN)
        text10.to_edge(DOWN)
        text11.to_edge(DOWN)    
        text12.to_edge(DOWN)
        for i in text13:
            i.scale(4)
            i.move_to([0,0,0])
        text14.to_edge(DOWN)    
        text15.to_edge(DOWN)  
        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3))
        self.wait(2)
        self.play(ReplacementTransform(text3,text4))
        self.wait(2)
        self.play(ReplacementTransform(text4,text6))
        self.wait(2)
        self.play(ReplacementTransform(text6,text7))
        self.wait(2)
        self.play(ReplacementTransform(text7,text8)) 
        self.wait(2)
        self.play(ReplacementTransform(text8,text82))
        self.wait(2)
        self.play(ReplacementTransform(text82,text9))
        self.wait(2)
        self.play(ReplacementTransform(text9,text10))
        self.wait(10)  
        self.play(ReplacementTransform(text10,text11))
        self.wait(2)
        self.play(ReplacementTransform(text11,text12))
        self.wait(2)
        self.play(FadeOut(text12))  
        self.wait(2)
        self.play(Write(text13[0]))
        for i in range(1,6):
            self.play(ReplacementTransform(text13[i-1],text13[i]))
            self.wait(1)
        self.play(FadeOut(text13[5]),Write(text14))
        self.wait(2)
        self.play(ReplacementTransform(text14,text15))
        self.wait(2)
        self.play(ReplacementTransform(text15,text151))      
        self.wait(2)
        self.play(ReplacementTransform(text151,text16))      
        self.wait(2)
        self.play(ReplacementTransform(text16,text17))
        self.wait(2)
        self.play(ReplacementTransform(text17,text18))
        self.wait(2)'''

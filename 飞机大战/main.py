# -*- coding:utf-8 -*-


import pygame
from pygame.locals import *
import time
import random


class Plane(object):

    def __init__(self, screen_temp, x, y, image_name):
        self.image = pygame.image.load(image_name)
        self.screen = screen_temp
        self.x = x
        self.y = y
        self.bullet = []    #飞机挂弹列表

    def display_plane(self):
        self.screen.blit(self.image, (self.x, self.y))
        #print(self.bullet)
        for temp in self.bullet:    #这个循环用于显示飞机所保存的子弹
            temp.move_bullet()  #先移动一下
            if temp.judge():    #判读是否越界。如果是，则删除
                self.bullet.remove(temp)
            temp.display_bullet()    #如果没有越界，则显示


class HeroPlane(Plane):  #猪脚飞机

    def __init__(self,screen_temp): #创建猪脚飞机
        Plane.__init__(self, screen_temp, 210, 500, "./feiji/hero1.png")

    # 显示飞机


    def move_left(self):        #控制飞机往左移动
        self.x-=20
    def move_right(self):       #控制飞机往右移动
        self.x+=20

    def fire(self):  #用于发射子弹

        self.bullet.append(HeroBullet(self.screen,self.x,self.y))


class EnemyPlane(Plane):

    """敌人飞机"""
    def __init__(self,screen_temp):
        self.bullet = []    #敌机子弹
        Plane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.track = "right"  # 用于控制飞机移动轨迹



    def move(self): #移动方法
        if self.track == "right":   #需要往右移动
            if self.x< 430:
                self.x+=4
            else:
                self.track = "left"
        elif self.track == "left":  #需要往左移动
            if self.x<=0:
                self.track = "right"
            else:
                self.x-=4

    def fire(self):
        random_num = random.randint(1,100)
        #print (random_num)
        if random_num == 76:
            print("敌人以发射子弹%s颗"%(str(len(self.bullet))))
            self.bullet.append(EnemyBullet(self.screen,self.x,self.y))


class Bullet(object):
    def __init__(self, screen_temp, x, y, image_name):
        #在screen中创建图像
        self.image = pygame.image.load(image_name)    #把图片保存到变量中
        self.screen = screen_temp
        self.x = x
        self.y = y
        self.display_bullet()




class HeroBullet(Bullet):

    def __init__(self,screen_temp,x,y):
        Bullet.__init__(self, screen_temp, x+40, y-20, "./feiji/bullet.png")

    def display_bullet(self):
        #print(self.x,self.y)
        self.screen.blit(self.image,(self.x,self.y))

    def move_bullet(self): #移动子弹轨迹，自动往上移动
        self.y-=5

    def judge(self):
        if self.y <= 0:

            return True
        else:
            return False


class EnemyBullet(Bullet):

    def __init__(self, screen_temp, x, y):

        Bullet.__init__(self,screen_temp, x+25, y+40, "./feiji/bullet1.png")

    def display_bullet(self):
        #print(self.x,self.y)
        self.screen.blit(self.image,(self.x,self.y))

    def move_bullet(self):
        self.y+=5

    def judge(self):

        if self.y >= 852:

            return True
        else:
            return False

def checkevent(hero_class):
    for event in pygame.event.get():  # 当pygame检测到事件的时候，会记录在此
        # print(event)

        if event.type == QUIT:  # 检测是否要退出
            print("exit")
            exit()
        # 检测是否按下了键盘
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:  # 往左移动
                hero_class.move_left()
            elif event.key == K_d or event.key == K_RIGHT:  # 往右移动
                hero_class.move_right()
            elif event.key == K_SPACE:  #发射子弹
                print("SPACE")
                hero_class.fire()


def main():
    screen = pygame.display.set_mode((480,852), 0, 32)  #创建窗口
    background = pygame.image.load("./feiji/background.png")    #导入背景图
    hero1 = HeroPlane(screen)   #创建对象
    enemy = EnemyPlane(screen)
    #循环绘画和判断是否有事件发生
    while True:
        screen.blit(background, (0, 0)) #加入背景
        hero1.display_plane()    #显示猪脚飞机
        enemy.display_plane()    #显示敌机
        enemy.fire()    #敌机开火
        enemy.move()    #自动移动
        pygame.display.update()     #刷新显示
        checkevent(hero1)
    time.sleep(0.1)

if __name__ == "__main__":
    main()



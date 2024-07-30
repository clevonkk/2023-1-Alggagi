"""
-*- Project_Alggagi_body -*-
Authors: Ko Gwanyoung(clevonkk23@snu.ac.kr), Joo Seungmin(smjoo2004@snu.ac.kr)
Last Modified: 20230531
"""

# -*- import -*-
import abc
import pygame
import math

# -*- variable -*-
screen_width, screen_height=800, 500
xboundary, yboundary=500, 500
screen=pygame.display.set_mode((screen_width, screen_height))
stage=['entrance']
settres=['null', 'null', 'null']
stone=[]; stoneA=[]; stoneB=[]
won=['null', 'null']
pygame.mixer.init(); clicksound=pygame.mixer.Sound('click.mp3')

# -*- class -*-
class Stone:
    shotstone=[]
    stoneAimg=pygame.image.load('./image/body/bodystoneA.png')
    stoneBimg=pygame.image.load('./image/body/bodystoneB.png')
    def __init__(self, x, y, vx, vy, mass, radius, color, f):
        self.x=x; self.y=y
        self.vx=vx; self.vy=vy; self.v=math.sqrt(self.vx**2+self.vy**2)
        self.m=mass; self.r=radius; self.color=color; self.f=f
    
    def draw(self, screen):
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.r-2)
        if self.color=='red':
            Stone.stoneAimg=pygame.transform.scale(Stone.stoneAimg, (2*self.r, 2*self.r))
            screen.blit(Stone.stoneAimg, (self.x-self.r, self.y-self.r))
        if self.color=='blue':
            Stone.stoneBimg=pygame.transform.scale(Stone.stoneBimg, (2*self.r+1, 2*self.r+1))
            screen.blit(Stone.stoneBimg, (self.x-self.r-0.5, self.y-self.r-0.5))
    
    def movement(self):
        self.x+=self.vx; self.y+=self.vy
        self.vx=self.f*self.vx; self.vy=self.f*self.vy; self.v=math.sqrt(self.vx**2+self.vy**2)
        if self.v<0.1: self.vx=0; self.vy=0

        if self.x<0 or self.x>xboundary-1 or self.y<0 or self.y>yboundary-1:
            stone.remove(self)
            if stoneA.count(self)!=0: stoneA.remove(self)
            if stoneB.count(self)!=0: stoneB.remove(self)

        if settres[0]=='mapB':
            if ((self.x>131) and (self.x<175)) and ((self.y>127) and (self.y<150)) or ((self.x>339) and (self.x<377)) and ((self.y>88) and (self.y<110)) or ((self.x>253) and (self.x<294)) and ((self.y>223) and (self.y<246)) or ((self.x>88) and (self.x<129)) and ((self.y>261) and (self.y<287)) or ((self.x>350) and (self.x<391)) and ((self.y>281) and (self.y<305)) or ((self.x>186) and (self.x<230)) and ((self.y>370) and (self.y<396)):
                self.vx=1.5*self.vx; self.vy=1.5*self.vy
        elif settres[0]=='mapC':
            if math.sqrt((self.x-245)**2+(self.y-250)**2)<=80 or math.sqrt((self.x-79)**2+(self.y-138)**2)<=30 or math.sqrt((self.x-388)**2+(self.y-64)**2)<=30 or math.sqrt((self.x-120)**2+(self.y-429)**2)<=30 or math.sqrt((self.x-355)**2+(self.y-401)**2)<=30:
                stone.remove(self)
                if stoneA.count(self)!=0: stoneA.remove(self)
                if stoneB.count(self)!=0: stoneB.remove(self)

    def press(self, mpos, event):
        try:
            if event.type==pygame.MOUSEBUTTONDOWN and math.sqrt((mpos[0]-self.x)**2+(mpos[1]-self.y)**2)<=self.r:
                clicksound.play() 
                Stone.shotstone.append(self)
            elif event.type==pygame.MOUSEBUTTONUP and len(Stone.shotstone)!=0:
                for item in stone:
                    if item==Stone.shotstone[0]:
                        v=0.5*math.sqrt((item.x-mpos[0])**2+(item.y-mpos[1])**2)
                        if v<=5:
                            item.vx=0.5*(item.x-mpos[0]); item.vy=0.5*(item.y-mpos[1])
                        else:
                            item.vx=2.5*(item.x-mpos[0])/v; item.vy=2.5*(item.y-mpos[1])/v
                Stone.shotstone.clear(); StoneShot.shotstate.clear()
        except Exception as exception: return
    def place(self, mpos, screen):
        if math.sqrt((mpos[0]-self.x)**2+(mpos[1]-self.y)**2)<=self.r:
            StoneShot.shotimg=pygame.transform.scale(StoneShot.shotimg, (60, 60))
            screen.blit(StoneShot.shotimg, (mpos[0]-30, mpos[1]-60))
        else: return

class StoneShot():
    shotstate=[]
    shotimg=pygame.image.load('./image/body/bodyslingshot.png')
    def __init__(self, stone, mpos):
        self.stone=stone; self.mpos=mpos
        StoneShot.shotstate.append(self)
    
    def draw(self, screen):
        pygame.draw.line(screen, (156, 31, 20), (self.stone.x, self.stone.y), self.mpos, 8)

        StoneShot.shotimg=pygame.transform.scale(StoneShot.shotimg, (60, 60))
        screen.blit(StoneShot.shotimg, (self.mpos[0]-30, self.mpos[1]-60))

class Button(metaclass=abc.ABCMeta):
    button=[[], [], [], []]
    def __init__(self, x, y, w, h, img):
        self.x=x; self.y=y; self.w=w; self.h=h #size of button: center, width, height
        self.img=pygame.image.load(img) #info of button: number and figure
    
    def draw(self, screen):
        self.img=pygame.transform.scale(self.img, (self.w, self.h))
        screen.blit(self.img, (self.x, self.y))
    
    def press(self, mpos):
        try:
            if ((self.x<=mpos[0]) and (mpos[0]<=self.x+self.w)) and ((self.y<=mpos[1]) and (mpos[1]<=self.y+self.h)):
                clicksound.play() 
                self.do(); return
        except Exception as exception:
            return
        else: return

    '''
    def place(self, mpos, screen):
        if ((self.x<=mpos[0]) and (mpos[0]<=self.x+self.w)) and ((self.y<=mpos[1]) and (mpos[1]<=self.y+self.h)):
            pygame.draw.rect(screen, 'yellow', ((self.x, self.y), (self.w, self.h)), 5)
        else: return
    '''

    '''
    def place(self, mpos, screen):
        if ((self.x<=mpos[0]) and (mpos[0]<=self.x+self.w)) and ((self.y<=mpos[1]) and (mpos[1]<=self.y+self.h)):
            click=pygame.image.load('./image/body/bodyplace.png').convert_alpha()
            if self.w <= self.h:
                click=pygame.transform.scale(click,(0.75*self.w, 0.75*self.w))
                if self.w== self.h:
                    screen.blit(click, (self.x+1/8*self.w, self.y+1/8*self.h))
                else: 
                    screen.blit(click, (self.x+1/8*self.w, self.y+7/16*self.h))
            else:
                if self.w >= 2*self.h:
                    click=pygame.transform.scale(click,(1.1*self.h, 1.1*self.h))
                else:
                    click=pygame.transform.scale(click,(0.75*self.h,0.75*self.h))
                screen.blit(click, (self.x+7/16*self.w, self.y-1/8*self.h))
        else: return
    '''

    '''
    def place(self, mpos, screen):
        if ((self.x<=mpos[0]) and (mpos[0]<=self.x+self.w)) and ((self.y<=mpos[1]) and (mpos[1]<=self.y+self.h)):
            pixels=pygame.PixelArray(self.img)
            for x in range(self.img.get_width()):
                for y in range(self.img.get_height()):
                    if pixels[x, y]=(240, 2):
                        print(pixels[x, y]); pixels[x, y]=(255, 255, 0)

        else: return
    '''
    
    def place(self, mpos, screen):
        pass

    @abc.abstractmethod
    def do(self):
        pass

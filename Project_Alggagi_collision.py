"""
-*- Project_Alggagi_collision -*-
Authors: Ko Gwanyoung(clevonkk23@snu.ac.kr), Joo Seungmin(smjoo2004@snu.ac.kr)
Last Modified: 20230531
"""

# -*- import -*-
import pygame
import math
import Project_Alggagi_controller as cnt
from Project_Alggagi_body import*

# -*- class -*-
class Pause(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[2].append(self)
    
    def do(self):
        if len(Button.button[2])==4:
            pass
        else:
            pygame.mixer.music.pause()
            pausewindow=PauseWindow(150, 100, 500, 312.5, './image/col/colpausewindow.png')
            resume=Resume(245, 300, 150, 35, './image/col/colresume.png')
            quit=Quit(440, 300, 100, 35, './image/col/colquit.png')
        
class PauseWindow(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[2].append(self)
        
    def place(self, mpos, screen):
        pass
        
    def do(self):
        pass

class Resume(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[2].append(self)
    
    def do(self):
        for item in Button.button[2]:
            if isinstance(item, PauseWindow) or isinstance(item, Quit):
                pygame.mixer.music.unpause()
                Button.button[2].remove(item)
        Button.button[2].remove(self)
            
class Quit(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[2].append(self)
        
    def do(self):
        Button.button[2].clear()
        stone.clear(); stoneA.clear(); stoneB.clear()
        stage[0]='entrance'

# -*- function -*-
def dist(bodyA, bodyB):
    return math.sqrt((bodyA.x-bodyB.x)**2+(bodyA.y-bodyB.y)**2)

def isCollided(stoneA, stoneB):
    if stoneA.vx*(stoneB.x-stoneA.x)+stoneA.vy*(stoneB.y-stoneA.y)>=0 or stoneB.vx*(stoneA.x-stoneB.x)+stoneB.vy*(stoneA.y-stoneB.y)>=0:
        dx=stoneA.x-stoneB.x
        dy=stoneA.y-stoneB.y
    
    return stoneA.r+stoneB.r>=dist(stoneA, stoneB)

def handleCollision(stoneA, stoneB): #collisions between stones
    if isCollided(stoneA, stoneB):
        shotsound.play()
        #m1=stone[i].m; m2=stone[j].m
        dVel=(stoneA.vx-stoneB.vx, stoneA.vy-stoneB.vy)
        dPos=(stoneA.x-stoneB.x, stoneA.y-stoneB.y)

        numerator=dVel[0]*dPos[0]+dVel[1]*dPos[1]
        denominator=dPos[0]*dPos[0]+dPos[1]*dPos[1]

        factor=numerator/denominator
        deltaV=(factor*dPos[0], factor*dPos[1])

        stoneA.vx=stoneA.vx-deltaV[0]; stoneA.vy=stoneA.vy-deltaV[1]
        stoneB.vx=stoneB.vx+deltaV[0]; stoneB.vy=stoneB.vy+deltaV[1]

def shot():
    if len(Stone.shotstone)!=0:
        if len(StoneShot.shotstate)==0:
            stoneshot=StoneShot(Stone.shotstone[0], pygame.mouse.get_pos())
        else: StoneShot.shotstate[0].mpos=pygame.mouse.get_pos()
    else: return

def updatePosition():
    for i in range(len(stone)):
        for j in range(i+1, len(stone)):
            handleCollision(stone[i], stone[j])
        
        #나갔을 때 빼내기 control. map 별로 어떻게 구현할 것인가? 통일성이 필요. 
    for item in stone:
        item.movement()

def allstop(stone):
    check=[]
    for item in stone:
        if item.vy==0 and item.vx==0: check.append(True)
        else : check.append(False)
    if False not in check: return True
    else : return False

def collision(stage):
    pygame.mixer.init()

    global stone, stoneA, stoneB
    global heartA, heartB
    global turn; turn='A'
    global shotsound; shotsound=pygame.mixer.Sound('shoot.mp3')

    if settres[0]=='mapA':
        num=int(settres[1])
        for i in range(settres[1]):
            globals()[f'a{i+1}']=Stone(295-45*num+i*90, 50, 0, 0, 5, 20, 'red', float(settres[2]))
            stoneA.append(globals()['a{}'.format(i+1)])
        for i in range(settres[1]):
            globals()[f'b{i+1}']=Stone(295-45*num+i*90, 450, 0, 0, 5, 20, 'blue', float(settres[2]))
            stoneB.append(globals()['b{}'.format(i+1)])
        stone.extend(stoneA); stone.extend(stoneB)
    
    if settres[0]=='mapB':
        num=int(settres[1])
        for i in range(settres[1]):
            globals()[f'a{i+1}']=Stone(380-45*num+i*70, 270-45*num+i*50, 0, 0, 5, 20, 'red', float(settres[2]))
            stoneA.append(globals()['a{}'.format(i+1)])
        for i in range(settres[1]):
            globals()[f'b{i+1}']=Stone(320-45*num+i*70, 400-45*num+i*50, 0, 0, 5, 20, 'blue', float(settres[2]))
            stoneB.append(globals()['b{}'.format(i+1)])
        stone.extend(stoneA); stone.extend(stoneB)
    
    if settres[0]=='mapC':
        num=5
        if int(settres[1])==4 or int(settres[1])==5:
            for i in range(settres[1]):
                globals()[f'a{i+1}']=Stone(260-45*num+i*60, 510-45*num-i*60, 0, 0, 5, 20, 'red', float(settres[2]))
                stoneA.append(globals()['a{}'.format(i+1)])
            for i in range(settres[1]):
                globals()[f'b{i+1}']=Stone(435-45*num+(4-i)*60, 680-45*num-(4-i)*60, 0, 0, 5, 20, 'blue', float(settres[2]))
                stoneB.append(globals()['b{}'.format(i+1)])
            stone.extend(stoneA); stone.extend(stoneB)
        else: 
            for i in range(1, 4):
                globals()[f'a{i+1}']=Stone(260-45*num+i*60, 510-45*num-i*60, 0, 0, 5, 20, 'red', float(settres[2]))
                stoneA.append(globals()['a{}'.format(i+1)])
            for i in range(1, 4):
                globals()[f'b{i+1}']=Stone(435-45*num+i*60, 680-45*num-i*60, 0, 0, 5, 20, 'blue', float(settres[2]))
                stoneB.append(globals()['b{}'.format(i+1)])
            stone.extend(stoneA); stone.extend(stoneB)

    heartA=pygame.image.load('./image/col/colheartA.png')
    heartA=pygame.transform.scale(heartA, (30, 30))
    heartB=pygame.image.load('./image/col/colheartB.png')
    heartB=pygame.transform.scale(heartB, (30, 30))

    pause=Pause(600, 432, 100, 47, './image/col/colpause.png')

    while stage[0]=='collision':
        display()

        if allstop(stone)==True and len(Stone.shotstone)==0 and len(StoneShot.shotstate)==0:
            if len(Button.button[2])==1:
                if turn=='A':
                    for item in stone: 
                        if item.color=='red': item.place(pygame.mouse.get_pos(), screen)
                elif turn=='B':
                    for item in stone: 
                        if item.color=='blue': item.place(pygame.mouse.get_pos(), screen)
            for i in range(len(Button.button[2])):
                if len(Button.button[2])==4:
                    if Button.button[2][i]!=pause:
                        Button.button[2][i].place(pygame.mouse.get_pos(), screen)
                else: Button.button[2][i].place(pygame.mouse.get_pos(), screen)

        for event in pygame.event.get():
            if event.type==pygame.QUIT: quit()
            elif event.type==pygame.MOUSEBUTTONDOWN and allstop(stone)==True:
                if len(Button.button[2])==1:
                    if turn=='A':
                        for item in stone:
                            if item.color=='red': item.press(pygame.mouse.get_pos(), event)
                    elif turn=='B':
                        for item in stone:
                            if item.color=='blue': item.press(pygame.mouse.get_pos(), event)
                for item in Button.button[2]:
                    item.press(cnt.mpress(pygame.mouse))

            elif event.type==pygame.MOUSEBUTTONUP:
                if len(Stone.shotstone)!=0 and turn=='A':
                    for i in range(int(len(stone)/2)): stone[i].press(pygame.mouse.get_pos(), event)
                    turn='B'
                elif len(Stone.shotstone)!=0 and turn=='B':
                    for i in range(int(len(stone)/2), len(stone)): stone[i].press(pygame.mouse.get_pos(), event)
                    turn='A'
            shot()

        updatePosition()

        if allstop(stone)==True:
            if len(stoneA)==0 and stage[0]!='entrance':
                if len(stoneB)==0:
                    Button.button[2].clear()
                    stone.clear(); stoneA.clear(); stoneB.clear()
                    won[0]='draw'; stage[0]='final'
                else:
                    Button.button[2].clear()
                    stone.clear(); stoneA.clear(); stoneB.clear()
                    won[0]='B'; won[1]='A'; stage[0]='final'
            elif len(stoneB)==0 and stage[0]!='entrance':
                Button.button[2].clear()
                stone.clear(); stoneA.clear(); stoneB.clear()
                won[0]='A'; won[1]='B'; stage[0]='final'

        pygame.display.flip()
    else: return

def display():
    if settres[0]=='mapA':
        map=pygame.image.load('./image/body/bodymapA.png')
        map=pygame.transform.scale(map, (screen_width+1, screen_height+1))
        screen.blit(map, (0, -1))
    elif settres[0]=='mapB':
        map=pygame.image.load('./image/body/bodymapB.png')
        map=pygame.transform.scale(map, (screen_width+1, screen_height+1))
        screen.blit(map, (0, -1))
    elif settres[0]=='mapC':
        map=pygame.image.load('./image/body/bodymapC.png')
        map=pygame.transform.scale(map, (screen_width+1, screen_height+1))
        screen.blit(map, (0, 0))
    
    for item in stone: item.draw(screen)
    for i in range(len(stoneA)):      
        screen.blit(heartA, (i*30+520, 119))
    for i in range(len(stoneB)):
        screen.blit(heartB,(i*30+520, 180))
    for item in Button.button[2]:
        item.draw(screen)
    for item in StoneShot.shotstate:
        item.draw(screen)

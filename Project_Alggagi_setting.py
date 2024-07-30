"""
-*- Project_Alggagi_setting -*-
Authors: Ko Gwanyoung(clevonkk23@snu.ac.kr), Joo Seungmin(smjoo2004@snu.ac.kr)
Last Modified: 20230531
"""

# -*- import -*-
import pygame
import Project_Alggagi_controller as cnt
from Project_Alggagi_body import*

# -*_ class -*-
class MapSelect(Button):
    def __init__(self, x, y, w, h, img, name):
        super().__init__(x, y, w, h, img)
        self.name=name
        Button.button[1].append(self)

    def do(self):
        settres[0]=self.name
        for item in Button.button[1]:
            if hasattr(item, 'boxtype') and item.boxtype=='Map':
                Button.button[1].remove(item)
        mapbox=Box(self.x, self.y, self.w, self.h, 'Map')
        count=0
        for item in Button.button[1]:
            if isinstance(item, Box): count+=1
        if count==3:
            for item in Button.button[1]:
                if isinstance(item, Error): Button.button[1].remove(item)

class StoneSelect(Button):
    def __init__(self, x, y, w, h, img, name):
        super().__init__(x, y, w, h, img)
        self.name=name
        Button.button[1].append(self)

    def do(self):
        settres[1]=self.name
        for item in Button.button[1]:
            if hasattr(item, 'boxtype') and item.boxtype=='Stone':
                Button.button[1].remove(item)
        mapbox=Box(self.x, self.y, self.w, self.h, 'Stone')
        count=0
        for item in Button.button[1]:
            if isinstance(item, Box): count+=1
        if count==3:
            for item in Button.button[1]:
                if isinstance(item, Error): Button.button[1].remove(item)

class FricSelect(Button):
    def __init__(self, x, y, w, h, img, name):
        super().__init__(x, y, w, h, img)
        self.name=name
        Button.button[1].append(self)

    def do(self):
        settres[2]=self.name
        for item in Button.button[1]:
            if hasattr(item, 'boxtype') and item.boxtype=='Fric':
                Button.button[1].remove(item)
        mapbox=Box(self.x-3, self.y-3, self.w+6, self.h+6, 'Fric')
        count=0
        for item in Button.button[1]:
            if isinstance(item, Box): count+=1
        if count==3:
            for item in Button.button[1]:
                if isinstance(item, Error): Button.button[1].remove(item)

class Box:
    def __init__(self, x, y, w, h, boxtype):
        self.x=x; self.y=y; self.w=w; self.h=h
        self.boxtype=boxtype
        self.img=pygame.Rect((self.x, self.y), (self.w, self.h))
        Button.button[1].append(self)
    
    def draw(self, screen):
        pygame.draw.rect(screen, 'yellow', self.img, 4)
    
    def place(self, mpos, screen):
        pass

    def press(self, mpos):
        pass

class Start(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[1].append(self)
    
    def do(self):
        search=0
        for i in range(len(Button.button[1])):
            if isinstance(Button.button[1][i], Box): search+=1
        if search==3:
            Button.button[1].clear()
            stage[0]='collision'
        else:
            count=0
            for item in Button.button[1]:
                if isinstance(item, Error): count+=1
            if count==0: error=Error(660, 120, 100, 80, './image/sett/setterror.png')

class Error(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[1].append(self)

    def place(self, mpos, screen):
        pass

    def do(self):
        pass

class Back(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[1].append(self)
        
    def do(self):
        Button.button[1].clear()
        stage[0]='entrance'

# -*- function -*-
def setting(stage):
    mapA=MapSelect(234.25, 174.25, 120.25, 120.25, './image/sett/settmapA.png', 'mapA')
    mapB=MapSelect(374.5, 174.25,  120.25, 120.25, './image/sett/settmapB.png', 'mapB')
    mapC=MapSelect(514.75, 174.25,  120.25, 120.25, './image/sett/settmapC.png', 'mapC')
    stoneA=StoneSelect(257, 320, 75, 75, './image/sett/settstone3.png', 3)
    stoneB=StoneSelect(397, 320,75, 75, './image/sett/settstone4.png', 4)
    stoneC=StoneSelect(537, 320, 75, 75, './image/sett/settstone5.png', 5)
    fricA=FricSelect(234.25, 420, 123, 30, './image/sett/settfricstrong.png', '0.93')
    fricB=FricSelect(376, 420, 120.25, 30, './image/sett/settfricmedium.png', '0.95')
    fricC=FricSelect(525, 420, 100, 30, './image/sett/settfriclight.png', '0.97')
    start=Start(670, 200, 70, 210, './image/sett/settstart.png')
    back=Back(755, 25, 20, 20, './image/sett/settback.png')

    while stage[0]=='setting':
        display()
        for i in range(len(Button.button[1])): Button.button[1][i].place(pygame.mouse.get_pos(), screen)
        for event in pygame.event.get():
            if event.type==pygame.QUIT: quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                for item in Button.button[1]:
                    item.press(cnt.mpress(pygame.mouse))
        pygame.display.flip()
    else: return

def display():
    img=pygame.image.load('./image/sett/settbackground.png')
    img=pygame.transform.scale(img, (screen_width+1.5, screen_height+4))
    screen.blit(img, (0, 2))

    for i in range(len(Button.button[1])):
        Button.button[1][i].draw(screen)

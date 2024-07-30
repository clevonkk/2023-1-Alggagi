"""
-*- Project_Alggagi_entrance -*-
Authors: Ko Gwanyoung(clevonkk23@snu.ac.kr), Joo Seungmin(smjoo2004@snu.ac.kr)
Last Modified: 20230531
"""

# -*- import -*-
import pygame
import Project_Alggagi_controller as cnt
from Project_Alggagi_body import*

# -*- class -*-
class Start(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[0].append(self)
    
    def do(self):
        if len(Button.button[0])==5: pass
        else:
            Button.button[0].clear()
            stage[0]='setting'
        
class Info(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[0].append(self)
        
    def do(self):
        if len(Button.button[0])==5: pass
        else:
            infowindow=InfoWindow(100, 50, 600, 375, './image/ent/entinfowindow.png')
            back=Back(672, 60, 20, 20, './image/ent/entback.png')

class InfoWindow(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[0].append(self)
        
    def place(self, mpos, screen):
        pass
        
    def do(self):
        pass

class Record(Button):
    file=open('./record.txt', 'r')
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[0].append(self)
    
    def do(self):
        if len(Button.button[0])==5: pass
        else:
            recordwindow=RecordWindow(100, 50, 600, 375, './image/ent/entrecordwindow.png')
            back=Back(672, 60, 20, 20, './image/ent/entback.png')

class RecordWindow(Button):
    lines=Record.file.readlines()[:5]
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[0].append(self)

    def draw(self, screen):
        self.img=pygame.transform.scale(self.img, (self.w, self.h))
        screen.blit(self.img, (self.x, self.y))
        
        count=0
        for item in Button.button[0]:
            if isinstance(item, RecordWindow): 
                font=pygame.font.Font('minecraft_font.ttf', 15)
                for i in range(len(RecordWindow.lines)):
                    text=font.render(RecordWindow.lines[i].strip(), True, (255, 255, 0))
                    screen.blit(text, (332, 210+37*i))
        
    def place(self, mpos, screen):
        pass
        
    def do(self):
        pass

class Back(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[0].append(self)
    
    def do(self):
        for item in Button.button[0]:
            if isinstance(item, (InfoWindow, RecordWindow)):
                Button.button[0].remove(item)
                Button.button[0].remove(self)

# -*- function -*-
def entrance(stage):
    start=Start(265, 286, 270, 40, './image/ent/entstart.png')
    info=Info(265, 340, 90, 40, './image/ent/entinfo.png')
    record=Record(385, 340, 150, 40, './image/ent/entrecord.png')
    

    while stage[0]=='entrance':
        display()
        for i in range(len(Button.button[0])):
            if len(Button.button[0])==4:
                if Button.button[0][i]!=info and Button.button[0][i]!=start:
                    Button.button[0][i].place(pygame.mouse.get_pos(), screen)
            else: Button.button[0][i].place(pygame.mouse.get_pos(), screen)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT: quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                for item in Button.button[0]:
                    item.press(cnt.mpress(pygame.mouse))
        pygame.display.flip()
    else: return
    
def display():
    img=pygame.image.load('./image/ent/entbackground.png')
    img=pygame.transform.scale(img, (screen_width+1, screen_height))
    screen.blit(img, (0, 0))

    for i in range(len(Button.button[0])):
        Button.button[0][i].draw(screen)

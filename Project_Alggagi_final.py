"""
-*- Project_Alggagi_final -*-
Authors: Ko Gwanyoung(clevonkk23@snu.ac.kr), Joo Seungmin(smjoo2004@snu.ac.kr)
Last Modified: 20230531
"""

# -*- import -*-
import pygame
import Project_Alggagi_controller as cnt
from Project_Alggagi_body import*

# -*_ class -*-
class Record(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[3].append(self)

    def do(self):
        count=0
        for item in Button.button[3]:
            if isinstance(item, SuccessRecord): count+=1
        if count==0:
            with open('./record.txt', 'r') as file:
                oldtext=file.read()

            with open('./record.txt', 'w') as file:
                if won[0]=='draw':
                    file.write('-'+'                                        '+'-\n'); file.write(oldtext)
                    file.flush()
                else: 
                    file.write(won[0]+'                                        '+won[1]+'\n'); file.write(oldtext)
                    file.flush()
            successrecord=SuccessRecord(250, 340, 300, 50, './image/fin/successrecord.png')
            
            Record.finfile.close()
class SuccessRecord(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[3].append(self)
    
    def place(self, mpos, screen):
        pass

    def do(self):
        pass

class Quit(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[3].append(self)
        
    def do(self):
        Button.button[3].clear()
        settres[0], settres[1], settres[2]='null', 'null', 'null'
        won[0]='null'
        stage[0]='entrance'

class Back(Button):
    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        Button.button[3].append(self)
    
    def do(self):
        for item in Button.button[3]:
            if isinstance(item, Record):
                Button.button[3].remove(item)
                Button.button[3].remove(self)

# -*- function -*-
def final(stage):
    quitgame=Quit(250, 385, 100, 40, './image/fin/finquit.png')
    record=Record(370, 385, 180, 40, './image/fin/finrecord.png')
    #back=Back(240, 240, 100, 100, './test.png')

    while stage[0]=='final':
        display()
        for i in range(len(Button.button[3])): Button.button[3][i].place(pygame.mouse.get_pos(), screen)
        for event in pygame.event.get():
            if event.type==pygame.QUIT: quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                for item in Button.button[3]:
                    item.press(cnt.mpress(pygame.mouse))
        pygame.display.flip()
    else: return

def display():
    if won[0]=='A':
        img=pygame.image.load('./image/fin/finplayerA.png')
    elif won[0]=='B':
        img=pygame.image.load('./image/fin/finplayerB.png')
    elif won[0]=='draw':
        img=pygame.image.load('./image/fin/findraw.png')
    img=pygame.transform.scale(img, (screen_width+1.5, screen_height+4))
    screen.blit(img, (0, 2))

    for i in range(len(Button.button[3])):
        Button.button[3][i].draw(screen)

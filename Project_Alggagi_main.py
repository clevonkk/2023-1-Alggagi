"""
-*- Project_Alggagi_main -*-
Authors: Ko Gwanyoung(clevonkk23@snu.ac.kr), Joo Seungmin(smjoo2004@snu.ac.kr)
Last Modified: 20230531
"""

# -*- import -*-
import pygame
import Project_Alggagi_entrance as ent
import Project_Alggagi_setting as sett
import Project_Alggagi_collision as col
import Project_Alggagi_final as fin
from Project_Alggagi_body import*

# -*- function -*-
def delay():
    delaying=True
    while delaying:
        img=pygame.image.load('./image/main/maindelay.png')
        img=pygame.transform.scale(img, (screen_width+1.5, screen_height+4))
        screen.blit(img, (0, 2))

        pygame.display.update()

        pygame.mixer.music.pause()
        pygame.time.delay(3000)

        delaying=False

# -*- main -*-

# initialization and settings
pygame.init()
pygame.display.set_caption("Alggagi")

#clock for fps
clock=pygame.time.Clock()

# mouse cursor shape
pygame.mouse.set_visible(True)
pygame.mouse.set_cursor(pygame.cursors.diamond)

# musics
backgroundsound=pygame.mixer.Sound("music,compute.mp3")
shotsound=pygame.mixer.Sound('shoot.mp3')
clicksound=pygame.mixer.Sound('click.mp3')

# run until the user asks to quit
running=True
while running:
    # main event loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT: running=False
    if stage[0]=='entrance':
        pygame.mixer.music.unload()
        pygame.mixer.music.load("music,compute.mp3")
        pygame.mixer.music.play()
        ent.entrance(stage)
    elif stage[0]=='setting':
        delay()
        pygame.mixer.music.unpause()
        sett.setting(stage)
    elif stage[0]=='collision':
        delay()
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load("whilegaming.mp3")
        pygame.mixer.music.play()
        col.collision(stage)
    elif stage[0]=='final':
        delay()
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load("winner.mp3")
        pygame.mixer.music.play()
        fin.final(stage)

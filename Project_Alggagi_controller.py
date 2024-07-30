"""
-*- Project_Alggagi_controller -*-
Authors: Ko Gwanyoung(clevonkk23@snu.ac.kr), Joo Seungmin(smjoo2004@snu.ac.kr)
Last Modified: 20230531
"""

# -*- function -*-
def mpress(mouse):
    bLeft, bMid, bRight=mouse.get_pressed()
    if bLeft:
        return mouse.get_pos()
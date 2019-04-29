# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:54:31 2019

@author: balam
"""

from dotBoxEnv import dotsBoxesEnv
from dotBoxEnv import display

dbe =dotsBoxesEnv(2)
dp = display(dbe.space, dbe.size, dbe.linePoints, dbe.boxPoints)
for act in dbe.allActions:
    dp.addAction(act)
dp.addBox(90,[255,255,0])
dp.addBox(5760,[0,255,255])
dp.releaseVideo()
dp.show()


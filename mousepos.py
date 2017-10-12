import ctypes
import pyautogui as pg
from tkinter import *
import os





while True :
    x,y= pg.position()

    print(x,y)
    
    #ctypes.windll.user32.MessageBoxW(0,"Current Mouse Position is ( {} ,{} )".format(x,y),"Mouse Position", 0)

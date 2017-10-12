import pyautogui as pg
import time
import random,string
import webbrowser as wb





def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def enterjunk(length):
    for i in range(1,length):
        pg.click(40, 150)
        pg.typewrite(randomword(random.randrange(0,10,1)))
        pg.click(100,150)
        time.sleep(3)

    return ""


if wb.open("http://www.cs.usfca.edu/~galles/visualization/BPlusTree.html",new=2) :
    time.sleep(3)
    enterjunk(100)
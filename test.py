#imports
import pygame as g
import random
import os
#inishiling modules
g.mixer.init()
g.init()
#window
screen_width = 900
screen_height = 600
gameWindow = g.display.set_mode((screen_width, screen_height))
g.display.set_caption("corona fight")
g.display.update()
#gameloop
def gameloop():
  #varibles
 exit_game = False
 #main loop
 while not exit_game:
            for event in g.event.get():
             print(event)
gameloop()
g.quit()
quit()
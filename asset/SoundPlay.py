import pygame
from time import sleep

pygame.init()

def clear():
    import os 
    os.system("cls")

def isOnSound(): 
    pygame.mixer.music.load("./assest/sounds/1.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        clear()
        sleep(1)

def isOffSound():
    pygame.mixer.music.load("./assest/sounds/2.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        clear()
        sleep(1)
    

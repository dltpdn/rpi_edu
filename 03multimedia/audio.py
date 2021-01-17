import pygame
import time

pygame.init()

#pygame.mixer.music.load("sample.wav")
pygame.mixer.music.load("sample.mp3")
while True:
    cmd = input("cmd{play:p, pause:pp, unpause:up, stop:s, quit:q} :")
    if cmd == "p":
        pygame.mixer.music.play()
    elif cmd == "pp":
        pygame.mixer.music.pause()
    elif cmd == "up":
        pygame.mixer.music.unpause()
    elif cmd == "s":
        pygame.mixer.music.stop()
    elif cmd == 'q':
        exit(0)
    else:
        print("incorrect cmd. try again.")

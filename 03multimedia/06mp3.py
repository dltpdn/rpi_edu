import pygame
import time

pygame.init()

#pygame.mixer.music.load("sample.wav")
pygame.mixer.music.load("sample.mp3")
while True:
    cmd = raw_input("cmd{play:p, pause:pp, unpause:up, stop:s} :")
    if cmd == "p":
        pygame.mixer.music.play()
    elif cmd == "pp":
        pygame.mixer.music.pause()
    elif cmd == "up":
        pygame.mixer.music.unpause()
    elif cmd == "s":
        pygame.mixer.music.stop()
      #  exit(0)
    else:
        print "incorrect cmd. try again."

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from time import sleep, perf_counter
import pygame
pygame.init()
pygame.mixer.init()

path=os.getcwd()+"/MetroBeat1.wav"

delay = d = 0.5
#print(60 / delay, 'bpm')
prev = perf_counter()
for i in range(20):
    sleep(d)
    sounda = pygame.mixer.Sound(path)
    sounda.play()
    t = perf_counter()
    delta = t - prev - delay
    #print('{:+.9f}'.format(delta))
    d -= delta
    prev = t



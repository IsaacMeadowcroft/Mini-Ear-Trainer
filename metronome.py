import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from time import sleep, perf_counter
import pygame
pygame.mixer.init()

strongBeatPath=os.getcwd()+"/metronome_sounds/MetroBar1.wav"
weakBeatPath=os.getcwd()+"/metronome_sounds/MetroBeat1.wav"

delay = d = 0.5
#print(60 / delay, 'bpm')
prev = perf_counter()
for i in range(20):
    sleep(d)
    if i % 4 == 0:
        sounda = pygame.mixer.Sound(strongBeatPath)
    else:
        sounda = pygame.mixer.Sound(weakBeatPath)
    sounda.play()
    t = perf_counter()
    delta = t - prev - delay
    #print('{:+.9f}'.format(delta))
    d -= delta
    prev = t


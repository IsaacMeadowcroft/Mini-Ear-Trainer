import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from time import sleep, perf_counter
import pygame
pygame.mixer.init()

strongBeatPath = "/Users/keith/Desktop/Ear Training/metronome_sounds/MetroBar1.wav"
weakBeatPath = "/Users/keith/Desktop/Ear Training/metronome_sounds/MetroBeat1.wav"


def executeMetronome(timeStamps):
    #60 / delay = 'bpm'
    delay = d = 1
    for i in range(20):
        sleep(d)
        
        if i % 4 == 0:
            sounda = pygame.mixer.Sound(strongBeatPath)
        else:
            sounda = pygame.mixer.Sound(weakBeatPath)
            
        sounda.play()
        timeStamps.append(perf_counter())
        
    return timeStamps

if __name__ == "__main__":
    print(executeMetronome([]))


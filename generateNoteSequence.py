import wave
import random
import os
from pydub import AudioSegment
from musicalNotes import *

def generateRandomNotes(notes, length):
    randomNotes = []
    for i in range(length):
        randomNotes.append(notes[random.randint(0,len(notes)-1)])
    return randomNotes

def constructWaveFile(randomNotes):
    currentPath = os.getcwd() + "/Sound3.wav"
    sound = []

    for i in range(len(randomNotes)):
        note = music.getNote(randomNotes[i])
        sound.append(AudioSegment.from_wav(note.filePath))

    for i in range(len(sound)):
        if i == 0:
            combined_sounds = sound[i]
        else:
            combined_sounds = combined_sounds + sound[i]

    combined_sounds.export(currentPath, format="wav")

if __name__ == "__main__":
    music = musicalNotes()
    notes = music.noteNames
    constructWaveFile(generateRandomNotes(notes, 6))
    

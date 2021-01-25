import wave
import random
import os
from pydub import AudioSegment

def generateRandomNotes(notes, length):
    randomNotes = []
    for i in range(length):
        randomNotes.append(notes[random.randint(0,len(notes)-1)])
    return randomNotes

def constructWaveFile(randomNotes):
    currentPath = os.getcwd()
    sound1 = AudioSegment.from_wav(currentPath + "/Sounds/C1.wav")
    sound2 = AudioSegment.from_wav(currentPath + "/Sounds/C2.wav")

    combined_sounds = sound1 + sound2
    combined_sounds.export(currentPath + "/Sound3", format="wav")

if __name__ == "__main__":
    notes=['A','C#','B','D']
    constructWaveFile(notes)

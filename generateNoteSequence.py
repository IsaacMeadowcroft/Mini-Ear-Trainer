import wave
import random
import os
from pydub import AudioSegment
from pydub.playback import play
from musicalNotes import *

rhythmValues = [1,2]

def generateRandomNotes(notes, length):
    randomNotes = []
    for i in range(length):
        curNote = notes[random.randint(0,len(notes)-1)]
        randomNotes.append(notes[random.randint(0,len(notes)-1)])
    return randomNotes

def generateRandomRhythm(length):
    randomRhythm = []
    for i in range(length):
        randomRhythm.append(random.choice(rhythmValues))
    return randomRhythm

def constructWaveFile(randomNotes, randomRhythm):
    currentPath = os.getcwd() + "/Sound3.wav"
    sound = []

    for i in range(len(randomNotes)):
        note = music.getNote(randomNotes[i])
        sound.append(generateRhythmicAudioSegment(note, randomRhythm[i]))

    for i in range(len(sound)):
        if i == 0:
            combined_sounds = sound[i]
        else:
            combined_sounds = combined_sounds + sound[i]

    combined_sounds.export(currentPath, format="wav")
    return combined_sounds

def generateRhythmicAudioSegment(note, length):
    audioSegment = AudioSegment.from_wav(note.filePath)
    audioSegment = audioSegment[:1500/length]
    return audioSegment

def playAudioSegment(sound):
    play(sound)

if __name__ == "__main__":
    music = musicalNotes()
    notes = music.noteNames
    randomNotes = generateRandomNotes(notes, 12)
    randomRhythm = generateRandomRhythm(12)
    print(randomNotes+randomRhythm)
    sound = constructWaveFile(randomNotes, [1, 2, 2, 2, 2, 1, 4, 4, 4, 4, 1, 1])
    print(sound)
    playAudioSegment(sound)
    

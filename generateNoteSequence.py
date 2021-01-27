import warnings
warnings.filterwarnings("ignore") 
import wave
import random
import os
from pydub import AudioSegment
from pydub.playback import play
from musicalNotes import *

music = musicalNotes()
rhythmChunks = [[1],[2,2],[0.5]]

def generateRandomNotes(notes, length):
    randomNotes = []
    for i in range(length):
        probability = random.random()
        if probability < .5:
            randomNotes.append(notes[0])
        elif probability < .8:
            randomNotes.append(random.choice([notes[2], notes[4]]))
        elif probability < .95:
            randomNotes.append(random.choice([notes[3], notes[1]]))
        elif probability < 1:
            randomNotes.append(random.choice([notes[5],notes[7],notes[6]]))
    return randomNotes

def generateRandomRhythm(length):
    randomRhythm = []
    rhythmLength = len(randomRhythm)
    rhythmChunk = None
    while rhythmLength < length:
        if length - rhythmLength >=2:
            rhythmChunk = random.choice(rhythmChunks)
        else:
            rhythmChunk = random.choice([[1],[0.5]])
        rhythmLength = rhythmLength + len(rhythmChunk)
        randomRhythm.extend(rhythmChunk)
    return randomRhythm

def constructWaveFile(randomNotes, randomRhythm):
    sound = []

    for i in range(len(randomNotes)):
        note = music.getNote(randomNotes[i])
        sound.append(generateRhythmicAudioSegment(note, randomRhythm[i]))

    for i in range(len(sound)):
        if i == 0:
            combined_sounds = sound[i]
        else:
            combined_sounds = combined_sounds + sound[i]

    return combined_sounds

def generateRhythmicAudioSegment(note, length):
    audioSegment = AudioSegment.from_wav(note.filePath)
    audioSegment = audioSegment[:1000/length]
    return audioSegment

def playAudioSegment(sound):
    play(sound)

def playScale(scaleNotes):
    scaleNotes = scaleNotes.copy()
    scaleNotes.extend(scaleNotes[-2::-1])
    rhythm = [4] * len(scaleNotes)
    playAudioSegment(constructWaveFile(scaleNotes, rhythm))

def noteRhythmToString(rhythmList):
    rhythmString = "["
    for i in range(0,len(rhythmList)-1):
        if rhythmList[i] == 2:
            rhythmString += "Eighth-Note, "
        elif rhythmList[i] == 1:
            rhythmString += "Quarter-Note, "
        else:
            rhythmString += "Half-Note, "
    if rhythmList[len(rhythmList)-1] == 2:
        rhythmString += "Eighth-Note]"
    elif rhythmList[i] == 1:
        rhythmString += "Quarter-Note]"
    else:
        rhythmString += "Half-Note]"
    return rhythmString
        
    

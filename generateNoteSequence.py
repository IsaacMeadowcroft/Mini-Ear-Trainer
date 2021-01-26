import warnings
warnings.filterwarnings("ignore") 
import wave
import random
import os
from pydub import AudioSegment
from pydub.playback import play
from musicalNotes import *

music = musicalNotes()
maxFourNoteRhythmChunk = [[1],[2,2],[2,4,4],[4,4,2],[4,4,4,4]]
maxThreeNoteRhythmChunk = [[1],[2,2],[2,4,4],[4,4,2]]
maxTwoNoteRhythmChunk = [[1],[2,2]]
maxOneNoteRhythmChunk = [[1]]


def generateRandomNotes(notes, length):
    randomNotes = []
    for i in range(length):
        probability = random.random()
        if probability < .6:
            randomNotes.append(notes[random.randint(0,len(notes)-1)])
        elif probability < .8:
            randomNotes.append(random.choice([notes[3], notes[5]]))
        elif probability < .9:
            randomNotes.append(random.choice([notes[8], notes[2]]))
        elif probability < 1:
            randomNotes.append(random.choice([notes[4],notes[6],notes[7]]))
    return randomNotes

def generateRandomRhythm(length):
    randomRhythm = []
    rhythmLength = len(randomRhythm)
    rhythmChunk = None
    while rhythmLength < length:
        if length - rhythmLength >= 4:
            rhythmChunk = random.choice(maxFourNoteRhythmChunk)
        elif length - rhythmLength >= 3:
            rhythmChunk = random.choice(maxThreeNoteRhythmChunk)
        elif length - rhythmLength >=2:
            rhythmChunk = random.choice(maxTwoNoteRhythmChunk)
        elif length - rhythmLength >=1:
            rhythmChunk = random.choice(maxOneNoteRhythmChunk)
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
    audioSegment = audioSegment[:3000/length]
    return audioSegment

def playAudioSegment(sound):
    play(sound)

def playScale(scaleNotes):
    scaleNotes.extend(scaleNotes[-2::-1])
    rhythm = [4] * len(scaleNotes)
    playAudioSegment(constructWaveFile(scaleNotes, rhythm))

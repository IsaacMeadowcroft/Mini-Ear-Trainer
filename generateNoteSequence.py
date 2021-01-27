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
        if probability < .5:
            randomNotes.append(notes[0])
        elif probability < .7:
            randomNotes.append(random.choice([notes[2], notes[4]]))
        elif probability < .85:
            randomNotes.append(random.choice([notes[3], notes[1]]))
        elif probability < 1:
            randomNotes.append(random.choice([notes[5],notes[7],notes[6]]))
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
    scaleNotes = scaleNotes.copy()
    scaleNotes.extend(scaleNotes[-2::-1])
    rhythm = [4] * len(scaleNotes)
    playAudioSegment(constructWaveFile(scaleNotes, rhythm))

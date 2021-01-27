import warnings
warnings.filterwarnings("ignore") 
import wave
import random
import os
from pydub import AudioSegment
from pydub.playback import play
from musicalNotes import *

music = musicalNotes()
rhythmChunks = [[1],[0.5],[0.25]]

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
        rhythmChunk = random.choice(rhythmChunks)
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

    return combined_sounds.overlay(generateMetronomeWaveFile(combined_sounds.duration_seconds))

def generateMetronomeWaveFile(length):
    one_sec_segment = AudioSegment.silent(duration=1000)
    beat1 = AudioSegment.from_wav(os.getcwd()+"/metronome_sounds/MetroBeat1.wav")
    beat2 = AudioSegment.from_wav(os.getcwd()+"/metronome_sounds/MetroBar1.wav")
    overlayed1 = one_sec_segment.overlay(beat1)
    overlayed2 = one_sec_segment.overlay(beat2)
    mergedSegment = (overlayed2+overlayed1+overlayed1+overlayed1)
    length-=4
    while(length>0):
        mergedSegment+=mergedSegment
        length-=4
    return mergedSegment

def generateRhythmicAudioSegment(note, length):
    audioSegment = AudioSegment.silent(duration=4000).overlay(AudioSegment.from_wav(note.filePath))
    size = int(500 / length)
    audioSegment = audioSegment[:size]
    return audioSegment

def playAudioSegment(sound):
    play(sound)

def playScale(scaleNotes):
    scaleNotes = scaleNotes.copy()
    scaleNotes.extend(scaleNotes[-2::-1])
    rhythm = [1] * len(scaleNotes)
    playAudioSegment(constructWaveFile(scaleNotes, rhythm))

def noteRhythmToString(rhythmList):
    rhythmString = "["
    for i in range(0,len(rhythmList)-1):
        if rhythmList[i] == 0.25:
            rhythmString += "Half-Note, "
        elif rhythmList[i] == 1:
            rhythmString += "Eigth-Note, "
        else:
            rhythmString += "Quarter-Note, "
    if rhythmList[len(rhythmList)-1] == 0.25:
        rhythmString += "Half-Note]"
    elif rhythmList[i] == 1:
        rhythmString += "Eigth-Note]"
    else:
        rhythmString += "Quarter-Note]"
    return rhythmString

if __name__ == "__main__":
    play(constructWaveFile(['C1','C1','C1'], [0.5,0.5,0.5]))
    

import warnings
warnings.filterwarnings("ignore") 
import wave
import random
import os
from pydub import AudioSegment
from pydub.playback import play
from musicalNotes import *

maxFourNoteRhythmChunk = [[1],[2,2],[2,4,4],[4,4,2],[4,4,4,4]]
maxThreeNoteRhythmChunk = [[1],[2,2],[2,4,4],[4,4,2]]
maxTwoNoteRhythmChunk = [[1],[2,2]]
maxOneNoteRhythmChunk = [[1]]


def generateRandomNotes(notes, length):
    randomNotes = []
    for i in range(length):
        curNote = notes[random.randint(0,len(notes)-1)]
        randomNotes.append(notes[random.randint(0,len(notes)-1)])
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

    return combined_sounds

def generateRhythmicAudioSegment(note, length):
    audioSegment = AudioSegment.from_wav(note.filePath)
    audioSegment = audioSegment[:1500/length]
    return audioSegment

def playAudioSegment(sound):
    play(sound)

def playScale(scaleNotes):
    rhythm = [2] * len(scaleNotes)
    playAudioSegment(constructWaveFile(scaleNotes, rhythm))

if __name__ == "__main__":
    music = musicalNotes()
    notes = music.getRandomMinorScale()
    print("TONIC IS: "+str(notes[0]))
    playScale(notes)
    randomNotes = generateRandomNotes(notes, 5)
    randomRhythm = generateRandomRhythm(5)
    print(str(randomRhythm)+" "+str(randomNotes))
    sound = constructWaveFile(randomNotes, randomRhythm)
    playAudioSegment(sound)
    

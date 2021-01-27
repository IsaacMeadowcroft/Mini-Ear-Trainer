from musicalNotes import *
from generateNoteSequence import *
import time
import metronome
import piano

def displayTonicAndPlayScale(defaultScale = "MAJOR"):
    if defaultScale == "MAJOR":
        notes = music.getRandomMajorScale()
    elif defaultScale == "MINOR":
        notes = music.getRandomMinorScale()
    print("TONIC IS: "+str(notes[0]))
    print("SCALE NOTES ARE: " + str(notes))
    playScale(notes)
    return notes

def generateRhythmAndNotes(notes, numberOfNotes = 3):
    randomNotes = generateRandomNotes(notes, numberOfNotes)
    randomRhythm = generateRandomRhythm(numberOfNotes)
    return (randomNotes, randomRhythm)

def playGeneratedNotes(randomNotes, randomRhythm):
    print("PLAYING RANDOMLY GENERATED NOTES")
    sound = constructWaveFile(randomNotes, randomRhythm)
    play(sound)

def executeEarTrainingExercise(defaultScale = "MAJOR", pianoPromptLength = 20000, numberOfNotes = 3):
    notes, rhythm = generateRhythmAndNotes(displayTonicAndPlayScale(defaultScale), numberOfNotes)
    time.sleep(1)
    playGeneratedNotes(notes, rhythm)
    recordedNotes, metronomeTimeStamps = piano.main(pianoPromptLength)
    evaluateExerciseResponse(recordedNotes, metronomeTimeStamps, notes, rhythm)

def evaluateExerciseResponse(recordedNotes, metronomeTimeStamps, notes, rhythm):
    playedNotes = []
    noteTimeStamps = []
    if recordedNotes != []:
        (playedNotes, noteTimeStamps) = list(map(list, zip(*recordedNotes)))
    if playedNotes != notes:
        print("INCORRECT ANSWER: YOU PLAYED "+str(playedNotes)+" BUT THE CORRECT ANSWER WAS "+str(notes))
    else:
        print("CORRECT ANSWER: "+str(notes)+" "+str(rhythm))
    

if __name__ == "__main__":
    music = musicalNotes()
    pianoPromptLength = 15000
    executeEarTrainingExercise("MAJOR", pianoPromptLength)
    
    



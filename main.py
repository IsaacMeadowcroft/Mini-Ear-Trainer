from musicalNotes import *
from generateNoteSequence import *
import metronome
import piano

def displayTonicAndPlayScale(defaultScale = "MAJOR"):
    if defaultScale == "MAJOR":
        notes = music.getRandomMajorScale()
    elif defaultScale == "MINOR":
        notes = music.getRandomMinorScale()
    print("TONIC IS: "+str(notes[0]))
    playScale(notes)
    return notes

def generateRhythmAndNotes(notes, numberOfNotes = 5):
    randomNotes = generateRandomNotes(notes, numberOfNotes)
    randomRhythm = generateRandomRhythm(numberOfNotes)
    return (randomNotes, randomRhythm)

def playGeneratedNotes(randomNotes, randomRhythm):
    sound = constructWaveFile(randomNotes, randomRhythm)
    play(sound)

def executeEarTrainingExercise(defaultScale = "MAJOR", numberOfNotes = 5):
    notes, rhythm = generateRhythmAndNotes(displayTonicAndPlayScale(defaultScale), numberOfNotes)
    playGeneratedNotes(notes, rhythm)
    print(str(notes)+" "+str(rhythm))
    
if __name__ == "__main__":
    music = musicalNotes()
    executeEarTrainingExercise()



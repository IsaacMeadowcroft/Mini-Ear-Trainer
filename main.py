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
    time.sleep(0.7)
    print("PLAYING RANDOMLY GENERATED NOTES")
    playGeneratedNotes(notes, rhythm)
    metronomeTimeStamps = piano.main()
    print("CORRECT ANSWER: "+str(notes)+" "+str(rhythm))
    return metronomeTimeStamps
    
if __name__ == "__main__":
    music = musicalNotes()
    metronomeTimeStamps = executeEarTrainingExercise("MINOR")
    print(metronomeTimeStamps)



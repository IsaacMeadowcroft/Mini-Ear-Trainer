import os
import random

class note:

    def __init__(self, filePath, noteName, notePosition):
        self.filePath = filePath
        self.noteName = noteName
        self.notePosition = notePosition


class musicalNotes:

    
    def __init__(self):
        currentPath = os.getcwd() + '/sounds/'
        self.noteNames = ['C1','C#1','D1','D#1','E1','F1','F#1','G1','G#1','A1','A#1','B1',\
                          'C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2','A2','A#2','B2']
        self.noteDict = dict()
        self.positionDict = dict()
        self.noteList = []

        for i in range(len(self.noteNames)):
            notePath = currentPath + self.noteNames[i] + '.wav'
            curNote = note(notePath, self.noteNames[i], i)
            self.noteDict[self.noteNames[i]] = curNote
            self.positionDict[i] = self.noteNames[i]
            self.noteList.append(curNote)
            

    def getNote(self, noteName):
        return self.noteDict.get(noteName)

    def getMajorScaleNotes(self, tonic):
        start = tonic.notePosition
        scaleNotes = [self.noteNames[i] for i in (start, start+2, start+4, start+5, start+7, start+9, start+11, start+12)]
        return scaleNotes

    def getMinorScaleNotes(self, tonic):
        start = tonic.notePosition
        scaleNotes = [self.noteNames[i] for i in (start, start+2, start+3, start+5, start+7, start+8, start+11, start+12)]
        return scaleNotes

    def getRandomMajorScale(self):
        tonic = self.noteList[random.randint(0,11)]
        return self.getMajorScaleNotes(tonic)

    def getRandomMinorScale(self):
        tonic = self.noteList[random.randint(0,11)]
        return self.getMinorScaleNotes(tonic)
        

if __name__ == "__main__":
    m = musicalNotes()
    print(m.getRandomMajorScale())

            

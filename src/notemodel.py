import time
import model

class NoteModel(model.Model):
    inputDate = model.Column(type=model.Type.int)
    inputText = model.Column(type=model.Type.text)

    #multiplicative value to convert decimal points of time.time() to full integer values.
    #TIMEPRECISION = 10000000
    #def __init__(self):
        #self.noteDict[int(time.time() * self.TIMEPRECISION)] = noteText
        #self.noteDict = makeDummyNotes()

    #def printNote(self):
        #print(self.noteDict)

#def makeDummyNotes():
    #dummyNotes = []
    #dummyNotes.append(NoteModel("Today I went for a walk."))
    #dummyNotes.append(NoteModel("Today i ate some shoes"))
    #dummyNotes.append(NoteModel("tomorrow im going to school"))
    #dummyNotes.append(NoteModel("yesterday i had a bagel"))
    #dummyNotes.append(NoteModel("last year i ate 5 pies"))
    #return dummyNotes

#someNotes = makeDummyNotes()
#someNotes[0].printNote()

model.Database.setup(host="localhost", database = "voicenotes", user="root", password="")

for i in range(5):
    i = NoteModel()
    i.inputDate = int(time.time() * self.TIMEPRECISION)
    i.inputText = "test"
    i.save()

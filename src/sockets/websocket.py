from tornado.websocket import WebSocketHandler
from textProcessing.ProcessText import ProcessText
from asynchronous.countdown import EventLoop, Countdown
from note import Notes
import string_to_date as std
import uuid

DURATION_CONST = 20

class WebSocket(WebSocketHandler):

    eventLoop = None
    countDown = None
    uuid = None

    state = "greeting"
    notes = Notes()
    '''
    Crucial methods to WebSocket class
    '''
    def check_origin(self, origin):
        return True

    def open(self):
        print("SERVER: On new connection!")
        self.sayGreetingsAndOptions()

    def on_message(self, str):
        print("on_message: ", str)
        if self.state is "ready":
            self.handleReadyState(str)
        elif self.state is "reading":
            self.handleReadingState(str)
        elif self.state is "writing":
            self.handleWritingState(str)

    def handleWritingState(self, str):
        print("writing: ", str)
        if str == "DONE_BUTTON":
            self.write_message(note.lastNote)
            # self.write_message("noted.")
            self.signalReady()
            return
        success = self.saveNote(str)
        print("writing success: ", success)
        if not success:
            self.write_message("could not write that last bit")

    def handleReadingState(self, str):
        print("reading: ", str)
        begin, end = std.getDateUnix(str)
        print(begin, end)
        notes = self.notes.findInRange(begin, end)
        print(notes)
        self.write_message(list(notes.values())[0])
        # expect str to be date time
        # when done reading, go to ready
        self.signalReady()

    def handleReadyState(self, str):
        if str == "read":
            self.write_message("When would you like me to read?")
            self.state = "reading"
        elif str == "write" or str == "right":
            self.write_message("What would you like to note?")
            self.state = "writing"
        else:
            self.write_message("say read or write")
        return

    def summarize(self, arr):
        return arr[0]

    def on_close(self):

        print("Socket closed.")

    def sayGreetingsAndOptions(self):
        self.write_message("Hello! Would you like to read or write?")
        self.state = "ready"

    def signalReady(self):
        self.write_message("Would you like to read or would you like to write?")
        self.state = "ready"

    def saveNote(self, str):
        if not self.isValid(str):
            print("saveNote isLongEnough")
            return False
        self.notes.pushNote(str)
        print("saveNote pushedNote")
        return True

    def isValid(self, str):
        return len(str) > 10

    def clearEventLoop(self):
        self.eventLoop.stop()
        self.eventLoop = None

    def clearCountDown(self, socket):
        socket.countDown.stop()
        socket.countDown = None

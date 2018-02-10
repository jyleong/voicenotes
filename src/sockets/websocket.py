from tornado.websocket import WebSocketHandler
from textProcessing.ProcessText import ProcessText
from asynchronous.countdown import EventLoop, Countdown
from note import Notes
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
            if str == "read":
                self.write_message("When would you like me to read?")
                self.state = "reading"
            elif str == "write" or str == "right":
                self.write_message("What would you like to note?")
                self.state = "writing"
            else:
                self.write_message("say read or write")
            return
        elif self.state is "reading":
            # expect str to be date time
            # when done reading, go to ready
            self.write_message("now reading. please wait")
            self.signalReady()
        elif self.state is "writing":
            if str == "DONE_BUTTON":
                self.write_message("noted.")
                self.signalReady()
                return
            success = self.saveNote(str)
            if not success:
                self.write_message("could not write that last bit")

        return str

    def on_close(self):

        print("Socket closed.")

    def sayGreetingsAndOptions(self):
        self.write_message("Hello! Would you like to read or write?")
        self.state = "ready"

    def signalReady(self):
        self.write_message("Would you like to read or would you like to write?")
        self.state = "ready"

    def saveNote(str):
        if self.isLongEnough(str):
            notes.pushNote(str)
            return True
        else:
            return False

    def isLongEnough(str):
        return len(str) > 20

    def clearEventLoop(self):
        self.eventLoop.stop()
        self.eventLoop = None

    def clearCountDown(self, socket):
        socket.countDown.stop()
        socket.countDown = None

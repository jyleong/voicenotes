from tornado.websocket import WebSocketHandler
from textProcessing.ProcessText import ProcessText
from asynchronous.countdown import EventLoop, Countdown
import uuid

DURATION_CONST = 20

class WebSocket(WebSocketHandler):

    eventLoop = None
    countDown = None
    uuid = None

    '''
    Crucial methods to WebSocket class
    '''
    def check_origin(self, origin):
        return True

    def open(self):
        print("SERVER: On new connection!")
        self.sayGreetingsAndOptions()

    def on_message(self, str):
        userCmd = ProcessText.switch(str)
        if userCmd == "READ":
            ## goto read state
            return
        else:
            ## goto write state
            return
        return str

    def on_close(self):

        print("Socket closed.")




    def clearEventLoop(self):
        self.eventLoop.stop()
        self.eventLoop = None

    def clearCountDown(self, socket):
        socket.countDown.stop()
        socket.countDown = None

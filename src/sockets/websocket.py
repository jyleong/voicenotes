from tornado.websocket import WebSocketHandler
from textProcessing.ProcessText import ProcessText
from asynchronous.countdown import EventLoop, Countdown

import uuid

DURATION_CONST = 20

class WebSocket(WebSocketHandler):

    eventLoop = None
    countDown = None
    uuid = None

    state = "greeting"
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
        if self.state is "greeting":
            if str == "read":
                self.write_message("now reading")
                self.state = "reading"
            elif str == "write":
                self.write_message("now writing")
                self.state = "writing"
            else:
                self.write_message("say read or write")
            return
        elif self.state is "reading":
            self.write_message("now reading. please wait")
        elif self.state is "writing":
            self.write_message("now writing. please wait")
        return str

    def on_close(self):

        print("Socket closed.")

    def sayGreetingsAndOptions(self):
        self.write_message("Hello! Would you like to read or write?")
        self.state = "greeting"


    def clearEventLoop(self):
        self.eventLoop.stop()
        self.eventLoop = None

    def clearCountDown(self, socket):
        socket.countDown.stop()
        socket.countDown = None

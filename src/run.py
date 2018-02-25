import os

from tornado.ioloop import IOLoop

from sockets.websocket import WebSocket
from tornado.web import Application



if __name__ == '__main__':
    print("PYTHONPATH: {}".format(os.environ['PYTHONPATH']))

    server = Application([
        (r'/websocket/', WebSocket)
    ])
    print("Running server on port 5000!")
    server.listen(5000)
    IOLoop.instance().start()
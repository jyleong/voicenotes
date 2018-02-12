import os

from tornado.ioloop import IOLoop
from tornado.web import Application, FallbackHandler
from tornado.wsgi import WSGIContainer
from tornado_sqlalchemy import (as_future, declarative_base,
                                make_session_factory, SessionMixin)


import app_file
from sockets.websocket import WebSocket
from tornado.gen import coroutine
from tornado.web import RequestHandler, Application
from src.models import Message

app = app_file.create_app(app_file.config_name)

class SyncWebRequestHandler(RequestHandler, SessionMixin):
    def get(self):
        with self.make_session() as session:
            count = session.query(Message).count()

        self.write('{} messages so far!'.format(count))


class AsyncWebRequestHandler(RequestHandler, SessionMixin):
    @coroutine
    def get(self):
        with self.make_session() as session:
            count = yield as_future(session.query(Message).count)

        self.write('{} messages so far!'.format(count))


if __name__ == '__main__':
    print("PYTHONPATH: {}".format(os.environ['PYTHONPATH']))
    session_factory = make_session_factory(os.environ['development_db'])

    server = Application([
        (r'/websocket/', WebSocket),
        (r'/sync', SyncWebRequestHandler),
        (r'/async', AsyncWebRequestHandler)
    ], session_factory=session_factory)
    print("Running server on port 5000!")
    server.listen(5000)
    IOLoop.instance().start()
#!/usr/bin/env python
""" Module: app

SendJack, Inc.'s Executive Summary for Jackalope.

"""
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns


class SummalopeApp(tornado.web.Application):

    """ The Tornado instance for Summalope. """


    def __init__(self):
        """ Construct a Tornado application. """
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    """ main loop for Python script. """
    app = SummalopeApp()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

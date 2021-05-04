#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options
import handlers
import os

define("port", default=8888, type=int)

urls = [
    (r"/", handlers.BaseHandler)
]

settings = dict({
    "template_path": os.path.join(os.path.dirname(__file__), "templates"), # create a folder templates and put the html file there
    #"static_path": os.path.join(os.path.dirname(__file__), "static"), # if there is static files, uncomment this.
    "cookie_secret": str(os.urandom(45)),
    "xsrf_cookies": True,
    "debug": False,
    "gzip": True,
})

application = tornado.web.Application(urls, **settings)


if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

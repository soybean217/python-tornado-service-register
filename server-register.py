# coding: utf-8

import tornado.ioloop
import tornado.web
import struct
import torndb
import time
import geoip2.database

import config
from Bastion import _test

TEST_CONTENT =  "";

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")
    def post(self, *args, **kwargs):
        self.write("")            

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ss/getc", MainHandler),
        (r"/ss/sendc", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(config.GLOBAL_SETTINGS['port'])
    tornado.ioloop.IOLoop.current().start()
# coding: utf-8

import tornado.ioloop
import tornado.web
import struct
import torndb
import time
import geoip2.database

import config
from Bastion import _test

TEST_CONTENT =  "<datas><cfg><durl></durl><vno></vno><stats>1</stats></cfg><da><data><kno>135</kno><kw>验证码*中国铁路</kw><apid>100</apid></data></da></datas>";

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")
    def post(self, *args, **kwargs):
        self.write("")        
        
class GetCHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(TEST_CONTENT)

class SendCHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")
        print(self.get_argument('msg'))
        print(self.get_argument('code'))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ss/getc", GetCHandler),
        (r"/ss/sendc", SendCHandler),
    ])

if __name__ == "__main__":
    print "begin..."
    app = make_app()
    app.listen(config.GLOBAL_SETTINGS['port'])
    tornado.ioloop.IOLoop.current().start()
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
        print("begin")
        # yield sleep_test()
        res = yield self.sleep()
        self.write("when i sleep %f s" % (time.time() - start))
        print("end")
    def post(self, *args, **kwargs):
        self.write("")  

    def sleep(self):
        time.sleep(5)
        return 5


        
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

def sleep_test():
    time.sleep(3)
    print("sleep finish")
    return 3

if __name__ == "__main__":
    print "begin..."
    app = make_app()
    app.listen(config.GLOBAL_SETTINGS['port'])
    tornado.ioloop.IOLoop.current().start()
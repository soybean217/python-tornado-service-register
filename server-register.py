# coding: utf-8

import tornado.ioloop
import tornado.web
import struct
import torndb
import time
import sys
import random

#private lib
import config
from Bastion import _test

reload(sys)
sys.setdefaultencoding("utf-8")

TEST_CONTENT =  "<datas><cfg><durl></durl><vno></vno><stats>1</stats></cfg><da><data><kno>106</kno><kw>验证码*。</kw><apid>100</apid></data><data><kno>135</kno><kw>验证码*。</kw><apid>100</apid></data></da></datas>";
SUCCESS_CONTENT = "<datas><stats>1</stats></datas>"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")

    def post(self, *args, **kwargs):
        self.write("")  

        
class GetCHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(TEST_CONTENT)
        print('getc imsi:'+str(self.get_argument('imsi')))

class SendCHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(SUCCESS_CONTENT)
        _msg = str(self.get_argument('msg'))
        _sendInfo = {}
        _sendInfo["msg"] = str(self.get_argument('msg'))
        _sendInfo["code"] = str(self.get_argument('code'))
        _sendInfo["imsi"] = str(self.get_argument('imsi'))
        _sendInfo["cid"] = str(self.get_argument('cid'))
        _sendInfo["apid"] = str(self.get_argument('apid'))
        print('sendinfo:'+str(_sendInfo))
        print('msg origin:'+_sendInfo["msg"])
        print('msg decode:'+str(_sendInfo["msg"].decode))
        insert_register_send_log(_sendInfo)

def insert_register_send_log(_info):
    dbLog=torndb.Connection(config.GLOBAL_SETTINGS['log_db']['host'],config.GLOBAL_SETTINGS['log_db']['name'],config.GLOBAL_SETTINGS['log_db']['user'],config.GLOBAL_SETTINGS['log_db']['psw'])
    sql = 'insert into log_async_generals (`id`,`logId`,`para01`,`para02`,`para03`,`para04`,`para05`) values (%s,%s,%s,%s,%s,%s,%s)'
    dbLog.insert(sql,long(round(time.time() * 1000))*10000+random.randint(0, 9999),311,_info["imsi"],_info["msg"],_info["code"],_info["cid"],_info["apid"])
    return 

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ss/getc", GetCHandler),
        (r"/ss/sendc", SendCHandler),
    ])

if __name__ == "__main__":
    print("register begin...")
    app = make_app()
    app.listen(config.GLOBAL_SETTINGS['port'])
    tornado.ioloop.IOLoop.current().start()
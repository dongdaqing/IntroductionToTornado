# -*- coding: utf-8 -*-
__author__ = 'dongdaqing'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

import urllib
import json

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        #访问url：http://localhost:8888/?id=XNzYyMzM1MDg0&pid=69b81504767483cf&format=1&guid=9c553730ef5b6c8c542bfd31b5e25b69
        video_id = self.get_argument('id')
        youku_pid = self.get_argument('pid')
        video_format = self.get_argument('format')
        device_guid = self.get_argument('guid')
        #http的header，请求路径，请求值
        header={"User-Agent":"Youku;3.4;Android;4.2.1;Galaxy Nexus"}
        path_data = "http://test1.api.3g.youku.com/common/v3/play?"
        query_data={
            "id":video_id,
            "pid":youku_pid,
            "format":video_format,
            "guid":device_guid
        }
        #拼字段
        request_url=path_data + urllib.urlencode(query_data)
        client = tornado.httpclient.AsyncHTTPClient()
        #创建HTTPRequest对象
        http_request_obj = tornado.httpclient.HTTPRequest(url=request_url, method="GET", headers=header)
        #利用HTTPRequest对象访问
        response = yield tornado.gen.Task(client.fetch, http_request_obj)
        body = json.loads(response.body)
        self.write(body)
        self.finish()

    # @tornado.web.asynchronous
    # @tornado.gen.engine
    # def post(self):
    #     #参考：http://test.api.3g.youku.com/user/del/favorite?pid=69b81504767483cf&cid=98&guid=9c553730ef5b6c8c542bfd31b5e25b69
    #     youku_pid = self.get_argument('pid')
    #     video_cid = self.get_argument('cid')
    #     device_guid = self.get_argument('guid')
    #     # header={"User-Agent":"Youku;3.4;Android;4.2.1;Galaxy Nexus"}
    #     path_data = "http://test.api.3g.youku.com/user/del/favorite?"
    #     query_data = {
    #         "pid":youku_pid,
    #         "cid":video_cid,
    #         "guid":device_guid
    #     }
    #     request_url = path_data + urllib.urlencode(query_data)
    #     client = tornado.httpclient.AsyncHTTPClient()
    #     http_request_obj = tornado.httpclient.HTTPRequest(url=request_url, method="POST")
    #     response = yield tornado.gen.Task(client.fetch, http_request_obj)
    #     body = json.loads(response.body)
    #     self.write(body)
    #     self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler)],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
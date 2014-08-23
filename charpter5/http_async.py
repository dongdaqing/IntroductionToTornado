__author__ = 'dongdaqing'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument('id')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://test1.api.3g.youku.com/common/v3/play?"+\
            urllib.urlencode({"id":query, "pid":"69b81504767483cf", "format":4,"guid":"9c553730ef5b6c8c542bfd31b5e25b69"}),
            callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        self.write(body)
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler)],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
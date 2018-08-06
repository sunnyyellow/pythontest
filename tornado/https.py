#encoding=utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import ssl

class getToken(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")

application = tornado.web.Application([
    (r'/', getToken),
])

if __name__ == '__main__':
    ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_ctx.load_cert_chain(
        '/Users/xueshijing/ca/server/server.crt',
        '/Users/xueshijing/ca/server/server.key',
        '123456'
    )
    http_server = tornado.httpserver.HTTPServer(application, ssl_options=ssl_ctx)
    http_server.listen(8443) #最开始设置监听443，出现permission denied的报错。查相关资料发现，unix环境下小于1024的端口不能被普通用户绑定，只有root用户可以。
    tornado.ioloop.IOLoop.instance().start()
#encoding=utf-8
import tornado.httpclient
from tornado import ioloop
from tornado import gen
import requests

def handle_response(response):
    print "======async_http_request======="
    if response.error:
        print("Error: %s" % response.error)
    else:
        print(response.body)

@gen.coroutine
def async_http_client():
    print "111"
    http_client = tornado.httpclient.AsyncHTTPClient()
    url = 'https://localhost:8443'
    response = yield http_client.fetch(url, ca_certs='/Users/xueshijing/ca/server/server.crt')
    response2 = yield http_client.fetch(url, ca_certs='/Users/xueshijing/ca/server/server.crt')
    #response = yield http_client.fetch(httpReq)
    if response.error:
        print("Error: %s" % response.error)
    else:
        print(response.body)
    print(response2.body)
    print "222"

def http_client():
    print "======sync_http_request=======" 
    http_client = tornado.httpclient.HTTPClient()
    url = 'https://localhost:8443'
    httpReq = tornado.httpclient.HTTPRequest(url, ca_certs='/Users/xueshijing/ca/server/server.crt')
    response = http_client.fetch(httpReq)
    print response.body

def _requests():
    print "=====request========"
    response = requests.get('https://localhost:8443', verify = '/Users/xueshijing/ca/server/server.crt')
    #或者绕过验证证书，verify = False
    print response.text
    #运行此函数会抛出一个警告，是因为旧的python版本返回的ssl证书里面缺少一个字段。

def proto_test():
    person = addressbook.Person()
    person.id = 666
    person.name = 'amy'
    person.email = '342323@vd.vom'
    phone = person.phones.add()
    phone.number = '12244234'
    phone.type = addressbook.Person.HOME

    print person
    print '==========='
    s = person.SerializeToString()
    print s
    print '==========='

    

if __name__ == '__main__':
   #http_client()
   #async_http_client()
   ioloop.IOLoop.current().run_sync(async_http_client)
   #_requests()
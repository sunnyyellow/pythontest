#encoding=utf-8
import urllib
import urllib2
import re
import cookielib
import time

class DataMgr(object):

    def __init__(self, filename):
        self.filename = filename
        return

    def getData(self, timetag, key):
        pass

    def setData(self, timetag, data):
        pass

class SpiderBase(object):
    def __init__(self, dmgr,today):
        self.opener = None
        self.cj = None
        self.dmgr = dmgr
        self.today=today
        return

    def work(self):
        pass

    def fetch(self, url, data):
        r = None
        content = None
        if self.opener is not None:
            if data is None:
                try:
                    r = self.opener.open(url)
                    content = r.read()
                except:
                    raise
            else:
                try:
                    urldata = urllib.urlencode(data)
                    r = self.opener.open(url,urldata)
                    content = r.read()
                except:
                    raise
        else:
            try:
                content = urllib2.urlopen(url).read()
            except:
                raise
        return content

    def cookieInstall(self):
        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)




        

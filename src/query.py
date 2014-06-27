import urllib2
from json import loads

class Query(object):

  def __init__(self, text, host, port, secret):
    # do Query
    url = "http://%s:%s/%s/%s" % (host, port, secret, text)
    try:
      ans = urllib2.urlopen(url)
      data = ans.read()
      self.query = loads(data)
    except urllib2.URLError, r:
      self.query = r

  def getResponse(self):
    return self.query
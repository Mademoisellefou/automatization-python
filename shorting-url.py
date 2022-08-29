from __future__ import with_statement
import contextlib
try:
    from urllib.parse  import urlencode
except:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except: 
    from urllib2 import urlopen
import sys 
def make_tiny(url):
    x=urlencode({'url':url})
    #x="https://es.wikipedia.org/wiki/Martin_Garrix"
    request_url = ('https://tinyurl.com/api-create.php?'+x)
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')
def main():
    for tinyurl in map(make_tiny,sys.argv[1:]):
        print(tinyurl)
if __name__=="__main__":
    main()
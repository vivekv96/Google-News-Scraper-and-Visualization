import time
import urllib
import urllib.request
from urllib.request import urlopen
import re
from http.cookiejar import CookieJar
import http.cookiejar
import datetime
import pprint

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'http://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&output=rss'
        sourcecode = opener.open(page).read()
        #print(sourcecode)

        try:
            titles = re.findall(b'<title>(.*?)</title>', sourcecode)
            links = re.findall(b'<link>(.*?)</link>', sourcecode)
            for title in titles:
                print(title)

            for link in links:
                print(link)

        except Exception as e:
                print (e)

    except Exception as e:
        print(e)

main()
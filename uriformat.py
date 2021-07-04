#!/usr/bin/env python3
import re

def URLtoURI(url):
    url = str(url)
    if (url.find(".com") != -1):
        choppedurl = url[url.find("spotify"):]
        choppederurl = re.sub('(.com)', '', choppedurl)
        choppedesturl = re.sub('/', ':', choppederurl)
        choppedesterurl = choppedesturl[:choppedesturl.find("?")]
        return choppedesterurl
    else:
        return url
   
class Songlink():
    def __init__(self, link, owner):
        self.link = link
        self.owner = owner

    #def getLink(self):
        #return self.link

    #def getOwner(self):
        #return self.owner

    def printData(self):
        print(self.link, self.owner, sep = ', ')

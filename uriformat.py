#!/usr/bin/env python3
def URLtoURI(url):
    if(url.find(':') != -1):
        return False
    #convert to URI here
   
class Songlink():
    def __init__(self, link, owner):
        self.link = link
        self.owner = owner

    def getLink(self):
        return self.link

    def getOwner(self):
        return self.owner

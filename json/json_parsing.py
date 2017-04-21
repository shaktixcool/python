import urllib2
import json

def main():
    urlData = ""
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getCode()
    if webUrl.getCode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print "Error"+

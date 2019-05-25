# -*- coding:utf-8 -*-
import http.client
import urllib
from xml.dom.minidom import parseString
# password = "42db2ecfe7ba9890e3152d176b35c4d4"
password = "42db2ecfe7ba9890e3152d176b35c4d4"

def SearchPos():
    from openapi import dataLst
    header = {'Authorization': 'KakaoAK ' + password}
    conn = http.client.HTTPSConnection("dapi.kakao.com")

    keyVal = urllib.parse.quote(dataLst[0])
    conn.request("GET", "/v2/local/search/keyword.xml?y=37.514322572335935&x=127.06283102249932&radius=20000&query="+keyVal, headers=header)
    req = conn.getresponse()
    print(req.status, req.reason)
    rb = req.read().decode('utf-8')

    print(rb)
    x, y = ParseDOM(rb)


def ParseDOM(rb):
    parseData = parseString(rb)
    InfoPos = parseData.childNodes
    row = InfoPos[0].childNodes

    for item in row:
        x = item.childNodes[10].firstChild.nodeValue
        y = item.childNodes[11].firstChild.nodeValue
        return x, y

def ParseTree(rb):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(rb)
    t = tree.getiterator("result")

    for i in t:
        x = i.find("x")
        print(x)
    pass
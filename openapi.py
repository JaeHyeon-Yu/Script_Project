# -*- coding:cp949 -*-
import os
import sys
import xml
import urllib
from urllib.request import urlopen
from xml.dom.minidom import parseString
# from xml.etree import ElementTree
password = '484350454a7a6f733431776467704b' # 서울데이터포털 인증키

def LoadXML2API(key):
    import http.client
    url = "/" + password + "/xml/ListCulturalAssetsInfo/1/5/"
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", url)
    req = conn.getresponse()

    cultureDoc = req.read().decode('utf-8')

    if cultureDoc is None:
        print("Error!")
    else:
        parseData = parseString(cultureDoc)
        InfoCulture = parseData.childNodes
        row = InfoCulture[0].childNodes
        dataLst = []
        for item in row:
            if item.nodeName == "row":
                subitems = item.childNodes
                # tel = str(subitems[1].firstChild.nodeValue)
                dataLst.append((subitems[3].childNodes))

        for i in range(len(dataLst)):
            print(dataLst[i][0])

    pass
    url = "http://openAPI.seoul.go.kr:8088/" + password + "/xml/ListCulturalAssetsInfo/1/5/" + key
    resp = None

    req = urllib.request.Request(url)

    try:
        resp = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read().decode('utf-8')
        # print(parseString(response_body.decode('utf-8')).toprettyxml())
        body = xml.dom.minidom
        body = parseString(response_body).toprettyxml()



        # doc = parseString(response_body)

        # print(type(doc))
        # doc = parse(response_body)
        # doc = ET.parse(response_body)
        # doc = ET.parse(doc)
        return body

def LoadXML2API2(key):
    url = "http://openAPI.seoul.go.kr:8088/" + password + "/xml/ListCulturalAssetsInfo/1/5/" + key
    u = urlopen(url)
    doc = ElementTree.parse(u)

    return doc

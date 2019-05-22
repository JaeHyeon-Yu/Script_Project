# -*- coding:utf-8 -*-
from Defined_Var import *
from xml.dom.minidom import parseString
password = '484350454a7a6f733431776467704b' # 서울데이터포털 인증키

def LoadXML2API(key):
    import http.client
    url = "/" + password + "/xml/ListCulturalAssetsInfo/1/800/"
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

                if subitems[NAME_KOR].firstChild.nodeValue == key:  # 키값(한글명)과 xml의 한글명이 같으면
                    dataLst.append((subitems[7].firstChild.nodeValue))
                    break

        for i in range(len(dataLst)):
            print(dataLst[0][0])


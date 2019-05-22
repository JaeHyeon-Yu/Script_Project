# -*- coding:utf-8 -*-
from Defined_Var import *
from xml.dom.minidom import parseString
password = '484350454a7a6f733431776467704b'  # 서울데이터포털 인증키
num_of_data = str(100)
dataLst = []

def LoadXML2API(key):
    # API 에서 XML 을 읽어온다.
    import http.client
    url = "/" + password + "/xml/ListCulturalAssetsInfo/1/" + num_of_data + "/"
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

        for item in row:
            if item.nodeName == "row":
                subitems = item.childNodes

                if subitems[NAME_KOR].firstChild.nodeValue == key:  # 키값(한글명)과 xml 의 한글명이 같으면
                    dataLst.append(subitems[NAME_ENG].firstChild.nodeValue)
                    break
        PrintInfo()

def PrintInfo():
    # dataLst 에 저장된 정보를 출력한다..
    for i in range(len(dataLst)):
        # 영문명 출력 : 처음부터 끝까지 루프돌면서 한글자씩 출력
        for j in range(len(dataLst[i])):
            print(dataLst[0][j], end='')
    print()
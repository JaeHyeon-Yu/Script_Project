# -*- coding:utf-8 -*-
from Defined_Var import *
from xml.dom.minidom import parseString
password = '484350454a7a6f733431776467704b'  # 서울데이터포털 인증키
num_of_data = str(100)
dataLst = []

def LoadXML2API():
    # API 에서 XML 을 읽어온다.
    import http.client
    import mainframe
    url = "/" + password + "/xml/ListCulturalAssetsInfo/1/" + num_of_data + "/"
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", url)
    req = conn.getresponse()

    cultureDoc = req.read().decode('utf-8')
    dataLst.clear()
    if cultureDoc is None:
        print("Error!")
    else:
        parseData = parseString(cultureDoc)
        InfoCulture = parseData.childNodes
        row = InfoCulture[0].childNodes

        for item in row:
            if item.nodeName == "row":
                subitems = item.childNodes

                if subitems[NAME_KOR].firstChild.nodeValue == mainframe.inputLabel.get():  # 키값(한글명)과 xml 의 한글명이 같으면
                    AppendData(subitems[NAME_KOR].firstChild.nodeValue)
                    AppendData(subitems[NAME_CNS].firstChild.nodeValue)
                    AppendData(subitems[NAME_ENG].firstChild.nodeValue)
                    AppendData(subitems[LOCATION].firstChild.nodeValue)
                    AppendData(subitems[INFO].firstChild.nodeValue)
                    AppendData(subitems[27].firstChild.nodeValue)
                    break

    PrintInfo()


def PrintInfo():
    # dataLst 에 저장된 정보를 출력한다.
    # 처음부터 끝까지 루프돌면서 한글자씩 출력
    import mainframe

    mainframe.NameText.insert(mainframe.INSERT, dataLst[KOR])

    mainframe.NameText.insert(mainframe.INSERT, "(")
    mainframe.NameText.insert(mainframe.INSERT, dataLst[CNS])
    mainframe.NameText.insert(mainframe.INSERT, ")")

    mainframe.NameText.insert(mainframe.INSERT, "\n")
    mainframe.NameText.insert(mainframe.INSERT, dataLst[ENG])

    mainframe.InfoText.insert(mainframe.INSERT, dataLst[INF])

    if dataLst[LOC] == "강남구":
        mainframe.locData[0] += 1
    elif dataLst[LOC] == "강동구":
        mainframe.locData[1] += 1
    elif dataLst[LOC] == "강북구":
        mainframe.locData[2] += 1
    elif dataLst[LOC] == "강서구":
        mainframe.locData[3] += 1
    elif dataLst[LOC] == "관악구":
        mainframe.locData[4] += 1
    elif dataLst[LOC] == "광진구":
        mainframe.locData[5] += 1
    elif dataLst[LOC] == "구로구":
        mainframe.locData[6] += 1
    elif dataLst[LOC] == "금천구":
        mainframe.locData[7] += 1
    elif dataLst[LOC] == "노원구":
        mainframe.locData[8] += 1
    elif dataLst[LOC] == "도봉구":
        mainframe.locData[9] += 1
    elif dataLst[LOC] == "동대문구":
        mainframe.locData[10] += 1
    elif dataLst[LOC] == "동작구":
        mainframe.locData[11] += 1
    elif dataLst[LOC] == "마포구":
        mainframe.locData[12] += 1
    elif dataLst[LOC] == "서대문구":
        mainframe.locData[13] += 1
    elif dataLst[LOC] == "서초구":
        mainframe.locData[14] += 1
    elif dataLst[LOC] == "성동구":
        mainframe.locData[15] += 1
    elif dataLst[LOC] == "성북구":
        mainframe.locData[16] += 1
    elif dataLst[LOC] == "송파구":
        mainframe.locData[17] += 1
    elif dataLst[LOC] == "양천구":
        mainframe.locData[18] += 1
    elif dataLst[LOC] == "영등포구":
        mainframe.locData[19] += 1
    elif dataLst[LOC] == "용산구":
        mainframe.locData[20] += 1
    elif dataLst[LOC] == "은평구":
        mainframe.locData[21] += 1
    elif dataLst[LOC] == "종로구":
        mainframe.locData[22] += 1
    elif dataLst[LOC] == "중구":
        mainframe.locData[23] += 1
    elif dataLst[LOC] == "중랑구":
        mainframe.locData[24] += 1

def AppendData(data):
    # 저장할 데이터를 인자로 받아 dataLst 에 저장한다.
    if data is None:
        dataLst.append("")
    else:
        dataLst.append(data)

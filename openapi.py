# -*- coding:cp949 -*-
import os
import sys
import urllib.request
from xml.dom.minidom import parseString
password = '484350454a7a6f733431776467704b' # 서울데이터포털 인증키

def LoadXML2API(key):
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
        response_body = resp.read()
        print(parseString(response_body.decode('utf-8')).toprettyxml())
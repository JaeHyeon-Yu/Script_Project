# -*- coding:utf-8 -*-
import http.client

# password = "42db2ecfe7ba9890e3152d176b35c4d4"
password = "42db2ecfe7ba9890e3152d176b35c4d4"

def SearchPos():
    header = {'Authorization': 'KakaoAK ' + password}
    conn = http.client.HTTPSConnection("dapi.kakao.com")
    conn.request("GET", "/v2/local/geo/coord2regioncode.xml?x=127.1086228&y=37.4012191", headers=header)

    req = conn.getresponse()
    print(req.status, req.reason)

    rb = req.read()
    print(rb.decode('utf-8'))
    pass





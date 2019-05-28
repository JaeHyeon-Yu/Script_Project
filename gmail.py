# -*- coding: utf-8 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "osm.html"

senderAddr = "zosua18@gmail.com"     # 보내는 사람 email 주소.
def SendMail(destination):
    from openapi import dataLst
    recipientAddr = str(destination)   # 받는 사람 email 주소.

    # msg = MIMEBase("multipart", "alternative")
    msg = MIMEText("한글명 : "+str(dataLst[0])+
                   "\n한문명 : "+str(dataLst[1])+
                   "\n영문명 : "+str(dataLst[2])+
                   "\n정보\n"+str(dataLst[4]))

    msg['Subject'] = "문화재 검색 결과 - " + str(dataLst[0])
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
    htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    # msg.attach(HtmlPart)

    # 메일을 발송한다.

    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("zosua18@gmail.com", "Yukina0107@")
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()


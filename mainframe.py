from tkinter import *
from tkinter import font
from openapi import LoadXML2API
import kakaomap

def InitMainframe(window):
    global mainframe
    mainframe = Frame(window)
    mainframe.pack()
    InitTopText(window)
    InitInputLabel(window)
    InitSearchButton(window)
    InitNameText(window)
    InitInfoText(window)
    InitMap(window)
    InitGmail(window)
    # InitGmailButton()
    # InitMapButton()

def InitTopText(window):
    # 타이틀 문장 출력
    TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="[서울시 문화재 검색]", fg="red").place(x=50, y=10)

def InitInputLabel(window):
    # 키값 입력창 삽입
    global inputLabel

    TempFont = font.Font(window, size=17, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="이름").place(x=10, y=60)
    inputLabel = Entry(window, font=TempFont, width=15, borderwidth=5, relief='ridge')
    inputLabel.place(x=70, y=55)

def InitSearchButton(window):
    # 검색버튼 삽입
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    searchButton = Button(window, font=TempFont, text="검색", borderwidth=3, command=SearchAction)
    searchButton.place(x=285, y=53)


def SearchAction():
    # 검색 실행
    NameText.configure(state='normal')
    NameText.delete(0.0, END)
    InfoText.configure(state='normal')
    InfoText.delete(0.0, END)
    LoadXML2API()

def InitNameText(window):
    # 검색 결과 출력창
    global NameText
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="명칭").place(x=13, y=110)

    NameText = Text(window, font=TempFont, width=30, height=2, borderwidth=5, relief='ridge')
    NameText.place(x=13, y=140)

    NameText.configure(state='disable')

def InitInfoText(window):
    global InfoText
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="정보").place(x=13, y=220)

    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    InfoText = Text(window, font=TempFont, width=37, height=17, borderwidth=5, relief='ridge')
    InfoText.place(x=13, y=250)

    InfoText.configure(state='disable')

def InitMapButton():
    # Map 출력 버튼
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    mapButton = Button(mainframe, font=TempFont, text="지도", command=kakaomap.SearchPos)
    mapButton.pack()

def InitMap(window):
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="지도").place(x=390, y=10)

    ph = PhotoImage(file="jido.gif")
    imgLabel = Label(window, image=ph)
    imgLabel.place(x=390, y=40)

def InitGmail(window):
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="메일").place(x=390, y=400)

    global mailLabel
    mailLabel = Entry(window, font=TempFont, width=25, borderwidth=5, relief='ridge')
    mailLabel.place(x=390, y=430)

    mailButton = Button(window, font=TempFont, text="보내기", command="")
    mailButton.place(x=687, y=427)
from tkinter import *
from tkinter import font
from openapi import LoadXML2API
def InitMainframe(window):
    global mainframe
    mainframe = Frame(window)
    mainframe.pack()
    ExuteMainframe()

def InitTopText():
    # 타이틀 문장 출력
    TempFont = font.Font(mainframe, size=20, weight='bold', family='Consolas')
    MainText = Label(mainframe, font=TempFont, text="[서울시 문화재 검색 App]")
    MainText.pack()

def InitInputLabel():
    global inputLabel
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    inputLabel = Entry(mainframe, font=TempFont, width=26, borderwidth=12, relief='ridge')
    inputLabel.pack()

def InitSearchButton():
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    searchButton = Button(mainframe, font=TempFont, text="검색", command=SearchAction)
    searchButton.pack()


def SearchAction():
    LoadXML2API("봉황각")
    pass


def ExuteMainframe():
    InitTopText()
    InitInputLabel()
    InitSearchButton()
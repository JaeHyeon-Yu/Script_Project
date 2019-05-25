from tkinter import *
from tkinter import font
from openapi import LoadXML2API

def InitMainframe(window):
    global mainframe
    mainframe = Frame(window)
    mainframe.pack()
    InitTopText()
    InitInputLabel()
    InitSearchButton()
    InitRenderText()

def InitTopText():
    # 타이틀 문장 출력
    TempFont = font.Font(mainframe, size=20, weight='bold', family='Consolas')
    MainText = Label(mainframe, font=TempFont, text="[서울시 문화재 검색 App]")
    MainText.pack()

def InitInputLabel():
    # 키값 입력창 삽입
    global inputLabel
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    inputLabel = Entry(mainframe, font=TempFont, width=26, borderwidth=12, relief='ridge')
    inputLabel.pack()

def InitSearchButton():
    # 검색버튼 삽입
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    searchButton = Button(mainframe, font=TempFont, text="검색", command=SearchAction)
    searchButton.pack()


def SearchAction():
    # 검색 실행
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    LoadXML2API()

def InitRenderText():
    # 검색 결과 출력창
    global RenderText
    TempFont = font.Font(mainframe, size=10, weight='bold', family='Consolas')
    RenderText = Text(mainframe, font=TempFont, width=49, height=27, borderwidth=12, relief='ridge')
    RenderText.pack()

    RenderText.configure(state='disable')
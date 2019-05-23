from tkinter import *
from tkinter import font

def InitMainframe(window):
    global mainframe
    mainframe = Frame(window)
    ExuteMainframe()

def InitTopText():
    # 타이틀 문장 출력
    TempFont = font.Font(mainframe, size=20, weight='bold', family='Consolas')
    MainText = Label(mainframe, font=TempFont, text="[서울시 문화재 검색 App]")
    MainText.pack()

def SearchBar():
    pass

def ExuteMainframe():
    InitTopText()
    mainframe.pack()
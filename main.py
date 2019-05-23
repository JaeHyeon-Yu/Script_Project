# -*- coding: utf-8 -*-
from openapi import *
from tkinter import *
from mainframe import *
active_loop = False
def PrintMenu():
    print("search : s")
    print("Exit : q")
def launcherFunction(menu):
    if menu is 's':
        key = str(input('input key : '))
        LoadXML2API(key)
    elif menu is 'q':
        exit()
while active_loop is True:
    PrintMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)

window = Tk()
window.title("문화재 검색 API")
window.geometry("400x600+750+200")
window.resizable(False, False)
InitMainframe(window)
window.mainloop()
# -*- coding: utf-8 -*-
# from openapi import *
from tkinter import *
from mainframe import *
from kakaomap import *


SearchPos()

window = Tk()
window.title("문화재 검색 API")
window.geometry("400x600+750+200")
window.resizable(False, False)
InitMainframe(window)
window.mainloop()
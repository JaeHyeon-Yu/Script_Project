# -*- coding: utf-8 -*-
from openapi import *
from tkinter import *
active_loop = True
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
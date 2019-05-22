# -*- coding: utf-8 -*-
from openapi import *
active_loop = True
def PrintMenu():
    print("search : s")
def launcherFunction(menu):
    if menu is 's':
        key = str(input('input key : '))
        LoadXML2API(key)
        # print(a)

        #print(type(a))
        #PrintItem(a)


        # aa = a.getElementsByTagName("NAME_KOR")

        # print(a.getElementsByTagName("NAME_KOR"))
def PrintItem(item):
    # print(type(item))
    print(item.find("NAME_KOR"))
    print(item)
    # print ("Name : ", item.attrib["NAME_KOR"])
    # for i in item.iter("")

    pass
while active_loop is True:
    PrintMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
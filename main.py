# -*- coding: utf-8 -*-
import openapi
active_loop = True
def PrintMenu():
    print("search : s")
def launcherFunction(menu):
    if menu is 's':
        key = str(input('input key : '))
        openapi.LoadXML2API(key)
while active_loop is True:
    PrintMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)

# http://openAPI.seoul.go.kr:8088/(인증키)/xml/ListCulturalAssetsInfo/1/5/(일련번호)
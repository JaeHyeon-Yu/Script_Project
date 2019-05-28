import folium
import requests

from tkinter import*
from io import BytesIO
import urllib
import urllib.request

from io import BytesIO
from PIL import Image, ImageTk
from urllib.request import urlopen

def make_googlemap_url(center, zoom=14, maptype='roadmap'):
    key = 'AIzaSyA9gjC63ldBuHDwYM6flkFJDbTq6vQhFdg'
    point = str(center[1]) + ',' + str(center[0])
    size = (500, 500)
    url = "http://maps.google.com/maps/api/staticmap?"
    url += "center=%s&" % point
    url += "zoom=%i&" % zoom
    url += 'scale=1&'
    url += "size=" + str(size[0]) + 'x' + str(size[1]) + '&'
    url += 'maptype=' + maptype + '&'
    url += '&markers=color:red%7Clabel:C%7C' + point + '&'
    url += 'key=' + key
    return url

def Draw_MapImage(x,y):
    map_url=make_googlemap_url((x, y))
    with urlopen(map_url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    map_image = ImageTk.PhotoImage(im)
    return map_image

def DrawMap(x, y, canvas):
    from openapi import dataLst
    map_osm = folium.Map(location=[y, x], zoom_start=17)
    folium.Marker([y, x], popup=dataLst[0]).add_to(map_osm)

    # Image_RestArea = Draw_MapImage(x, y)
    # canvas.create_image(160, 100, image=Image_RestArea)
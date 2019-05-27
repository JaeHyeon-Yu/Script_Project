import folium
from PIL import Image, ImageTk
import requests

from tkinter import*
from io import BytesIO
import urllib
import urllib.request
mData = folium.Map(location=[37.6603359879944,127.006201548641], zoom_start=17)
def DrawMap(x, y):
    from openapi import dataLst
    global mData
    map_osm = folium.Map(location=[y, x], zoom_start=17)
    folium.Marker([y, x], popup=dataLst[0]).add_to(map_osm)
    map_osm.save("osm.html")
    mData = map_osm.render()
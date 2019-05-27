import folium
from PIL import Image, ImageTk
import requests

from tkinter import*
from io import BytesIO
import urllib
import urllib.request
def DrawMap(x, y):
    from openapi import dataLst
    from main import window
    map_osm = folium.Map(location=[y, x], zoom_start=13)
    folium.Marker([y, x], popup=dataLst[0]).add_to(map_osm)
    map_osm.save("osm.html")


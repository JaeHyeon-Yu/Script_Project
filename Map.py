import folium

def DrawMap(x, y):
    from openapi import dataLst

    map_osm = folium.Map(location=[y, x], zoom_start=13)
    folium.Marker([y, x], popup=dataLst[0]).add_to(map_osm)
    map_osm.save("osm.html")
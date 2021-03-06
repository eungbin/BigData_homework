#_*_coding:utf-8 _*_

import folium
import json

map_osm = folium.Map(location=[37.566345,126.977893], zoom_start=8)
rfile = open('./provinces-geo.json', 'r', encoding='utf-8').read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name='json_data').add_to(map_osm)
map_osm.save('./provice2011.html')

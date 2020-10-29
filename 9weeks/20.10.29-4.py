import folium

map_osm = folium.Map(location=[37.566345,126.977893], zoom_start=17)
folium.Marker([37.566345,126.977893],popup=u'서울시청',
	icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
folium.CircleMarker([37.5658859,126.9754788],radius=100, color='#3186cc',
	fill_color='#3186cc', popup=u'덕수궁').add_to(map_osm)
map_osm.save('./seoulMap.html')

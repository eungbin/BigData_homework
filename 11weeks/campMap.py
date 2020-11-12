#_*_coding:utf-8 _*_
import pymysql
import folium

try:
    conn = pymysql.connect(host='localhost', user='root', password='vk2sjf12',db='bigdata',charset='utf8')
    curs = conn.cursor()
    sql = u"select * from camp where c_addr like \'%경기도%\' limit 0, 10"
    curs.execute(sql)
    result = curs.fetchall()
    conn.close()
    mapDF = list()
    for row in result:
        rowData = {'campName':row[1], 'campLAT':row[2],'campLNG':row[3],'campeAddress':row[4]}
        mapDF.append(rowData)
    map_osm = folium.Map(location=[37.275273,127.009413], zoom_start=10)
    for markers in mapDF:
        folium.Marker([markers['campLAT'],markers['campLNG']],popup=markers['campName'], icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
    map_osm.save('/Users/kim/Desktop/campMap.html')
    
except Exception as er:
    print(er)
else:
    print('Completed!!')
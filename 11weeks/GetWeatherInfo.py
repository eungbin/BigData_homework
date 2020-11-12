#_*_coding:utf-8 _*_
'''
Created on Nov 4, 2020

@author: parkmiyoung
'''
import math
import json
import urllib
import urllib.request as urls
import pandas as pd
import requests

def getWeater(cityname ,nx, ny):
    serviceKey="pphQtmfAuXVKBfVJBG5bq%2B8ccRLD1x4r4GS23rjW4p2qeDfHVYHy1c2hyER93Kqlaj0aIox4YJQqwRCpBJ0UqQ%3D%3D"
    endpoint ="http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?ServiceKey="+serviceKey
    basedate="20201112"
    basetime="0500"
#     basetimeList =['0200','0500','0800','1100','1400','1700','2000','2300']
    urlstr = "&pageNo=1&numOfRows=10&dataType=json&base_date="+basedate+"&base_time="+basetime+"&nx="+nx+"&ny="+ny
    endpoint += urlstr
    request = urls.Request(endpoint)
    request.get_method = lambda: 'GET'
    response_body = urls.urlopen(request).read()
    json_data = json.loads(response_body.decode('utf-8'))
    weatherDict=dict()
    degree = json_data['response']['body']['items']['item']
    for i in range(len(degree)):
        weatherDict['cityname'] = cityname
        if degree[i]['category'] == 'T3H':
            weatherDict['degree'] = degree[i]['fcstValue']
    return weatherDict
    
def getGPS(CiyNames):
    appKey="061031991a773bc15221ed3d2a0add88"
    addr = urllib.parse.quote(CiyNames)
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr+'&page=1&size=10'
    headers = {"Authorization": "KakaoAK "+appKey}
    result = json.loads(str(requests.get(url, headers=headers).text))
    lon = result['documents'][0]['x']
    lat = result['documents'][0]['y']
    return (lat,lon)
 
def grid(v1, v2) :

    RE = 6371.00877 # 지구 반경(km)
    GRID = 5.0      # 격자 간격(km)
    SLAT1 = 30.0    # 투영 위도1(degree)
    SLAT2 = 60.0    # 투영 위도2(degree)
    OLON = 126.0    # 기준점 경도(degree)
    OLAT = 38.0     # 기준점 위도(degree)
    XO = 43         # 기준점 X좌표(GRID)
    YO = 136        # 기1준점 Y좌표(GRID)

    DEGRAD = math.pi / 180.0
    RADDEG = 180.0 / math.pi

    re = RE / GRID;
    slat1 = SLAT1 * DEGRAD
    slat2 = SLAT2 * DEGRAD
    olon = OLON * DEGRAD
    olat = OLAT * DEGRAD

    sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(math.pi * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn);
    rs = {};

    ra = math.tan(math.pi * 0.25 + float(v1) * DEGRAD * 0.5)
    ra = re * sf / math.pow(ra, sn)

    theta = float(v2) * DEGRAD - olon
    if theta > math.pi :
        theta -= 2.0 * math.pi
    if theta < -math.pi :
        theta += 2.0 * math.pi
    theta *= sn
    rs['x'] = math.floor(ra * math.sin(theta) + XO + 0.5)
    rs['y'] = math.floor(ro - ra * math.cos(theta) + YO + 0.5)

    return (str(rs["x"]).split('.')[0],str(rs["y"]).split('.')[0])
data_korea = pd.read_csv('./data_draw_korea.csv', index_col=0, encoding='utf-8')
data_korea[u'주소'] = data_korea[u'광역시도'] +' '+ data_korea[u'행정구역']
posTupleList = list()
weather_List = list()

for addr in data_korea[u'주소']:
    posTuple = getGPS(addr)
    nxTuple = grid(posTuple[0], posTuple[1])
    weather_List.append(getWeater(addr,nxTuple[0],nxTuple[1])['degree'])
dk_humidity = pd.DataFrame({'기온':weather_List})
data_korea = data_korea.join(dk_humidity)
data_korea.to_csv('./data_weather_degree11.csv')
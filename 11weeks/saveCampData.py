#_*_coding:utf-8 _*_

import urllib.request as urls
import pymysql
from xml.etree.ElementTree import *
try:
    url = 'http://api.data.go.kr/openapi/tn_pubr_public_campg_api?serviceKey=6GBIi%2FHqTOvgf0eowT0jOWvRi6JCMIcfE%2B3O8KNzoy2Emmno8pzXpjFkEmkUa2Pn%2F%2FQyB5fLbuvzQbobseRB%2FA%3D%3D&pageNo=1&numOfRows=100&type=xml'
    request = urls.Request(url)
    request.get_method = lambda: 'GET'
    response_body = urls.urlopen(request).read()
    response_body = response_body.decode('utf-8')
    xmlData =fromstring(response_body)
    camplist=list()
    for parent in xmlData.iter("item"):
        camp = list()
        for item in parent:
            camp.append(item.text)
        camplist.append(camp)
    conn = pymysql.connect(host='localhost', user='root', password='vk2sjf12',db='bigdata',charset='utf8')
    curs = conn.cursor()
    for i in range(len(camplist)):
        sql = 'insert into camp(c_name,c_lat, c_lng,c_addr,c_siteCount,c_dayPerson,c_cvn)values (\'{0}\', {1}, {2}, \'{3}\',{4},{5},\'{6}\')'.format(camplist[i][0],float(camplist[i][2]),float(camplist[i][3]),camplist[i][4],int(camplist[i][7]),int(camplist[i][10]),camplist[i][12])
        curs.execute(sql)
    conn.commit()
    conn.close()

except Exception as er:
    print(er)
else:
    print('Completed!!')

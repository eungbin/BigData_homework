import json
import urllib
import urllib.request as urls
import pymysql
import ssl

context = ssl._create_unverified_context()
client_id = "DkCWcUboGFZrawW2meZj"
client_secret = "iOyRofPezd"
encText = urllib.parse.quote("python")
url = "https://openapi.naver.com/v1/search/book?query=" + encText+"&display=10&start=1"
request = urls.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response =urls.urlopen(request,context=context)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    json_data = json.loads(response_body.decode('utf-8'))
    print(json_data)

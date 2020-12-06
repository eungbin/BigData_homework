# from urllib.parse import urlparse
# from urllib.request import urlopen
# import urllib.request
# import urllib.parse
import requests

import urllib.request as urls
from urllib.parse import unquote

# url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
# api_key = "e4FQBECA5Z7s9oSL7BRnzNGsT7cKC%2Bn3edOBBd1%2Bi2a%2FPi%2FFv8F7n8tVqsdW9D%2FG970%2B3CPwhjUWps20nhmTUQ%3D%3D"
# api_key_decode = requests.utils.unquote(api_key)
# queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : api_key_decode, urllib.parse.quote_plus('pageNo') : '1', urllib.parse.quote_plus('numOfRows') : '10', urllib.parse.quote_plus('startCreateDt') : '20200310', urllib.parse.quote_plus('endCreateDt') : '20200315' })
#
# request = urllib.request.Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urllib.request.urlopen(request).read()
# print(response_body)

api_key = "e4FQBECA5Z7s9oSL7BRnzNGsT7cKC%2Bn3edOBBd1%2Bi2a%2FPi%2FFv8F7n8tVqsdW9D%2FG970%2B3CPwhjUWps20nhmTUQ%3D%3D"
api_key_decode = unquote(api_key)
test = '%2B3CPwhjUWps20nhmTUQ%3D%3D&pageNo=1&numOfRows=100&type=xml'
test_decode = unquote(test)
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + api_key_decode + test_decode
request = urls.Request(url)
request.get_method = lambda: 'GET'
response_body = urls.urlopen(request).read()
response_body = response_body.decode('utf-8')

print(response_body)
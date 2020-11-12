import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

context = ssl._create_unverified_context()

def getImageURL(url):
    htmlpiaxbay_image = requests.get(url).text
    soup_images = BeautifulSoup(htmlpiaxbay_image,"lxml")
    img = soup_images.find_all(class_='_img')
    imageUrls = list()
    for i in img:
        imgUrl = i['data-source']
        imageUrls.append(imgUrl)
    return imageUrls


URL = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=cat'
downPath = './cat'
naver_imagelist = getImageURL(URL)
print(naver_imagelist)
imgcount = 10

for k in range(imgcount):
    with urlopen(naver_imagelist[k], context=context) as f:
        with open(downPath + "/" + str(k) + '.jpg', 'wb') as h:  # w - write b - binary
            img = f.read()
            h.write(img)
print("donwload Completed!")

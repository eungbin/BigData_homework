#_*_coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url ="https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20201111"
html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music,"lxml")

titles = soup_music.select('td.title div.tit5 a')
singers = soup_music.select('td.point')

song_titles = list()
singerList = list()

for title in titles:
    song_titles.append(title.get_text())
for singer in singers:
    singerList.append(singer.get_text().strip())
for index in range(10):
    print("{0} {1} - {2}".format(index+1, song_titles[index], singerList[index]))

from bs4 import BeautifulSoup

f = open('./myNovelList.html', encoding='utf-8')
html = f.read()
f.close()
soup = BeautifulSoup(html, "lxml")

titles = soup.find_all('p', {"id":"title"})
authors = soup.find_all('p', {"id":"author"})

for index in range(len(titles)):
    print("title: {0}, author: {1}".format(titles[index].get_text(), authors[index].get_text()))
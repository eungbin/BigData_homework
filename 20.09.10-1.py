#_*_coding:utf-8 _*_

numberlist = [1, 2, 3, 4, 5]

for i in range(len(numberlist)):
    print("index:", i, "value:", numberlist[i]+1)

langDict = {"Korean": "Korea", "english":[ 'UK', 'USA', 'Austrailia', 'India'], 'chinese': 'china', 'japanese': 'japan'}

print('korean country', ':', langDict['Korean'])

english = langDict['english']

strlang = ''
for i in range(len(english)):
    if i <len(english)-1:
        strlang += english[i] + ', '
    else:
        strlang += english[i]

print("english contry : ", strlang)
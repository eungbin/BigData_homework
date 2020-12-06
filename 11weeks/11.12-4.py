#_*_coding:utf-8 _*_

import tweepy, io

consumer_key = "wmAViWttr6GRBCdt8NTAUs4mq"
consumer_secret = "PJXeDzxuRNGIdLdzB0xl9u9K778BATwOt1bPF3HBbqGO6ysW2E"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  #oAuth 인증 객체 생성

access_token = "1304320551779880960-fRKPw0hy0TeuDNsMZQTwUQar3EMDf0"
access_toen_secret = "c98kSO0vGC5TZznxnysnaBuxkMxndDD8ixDJYznyZsLtv"

auth.set_access_token(access_token, access_toen_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)  #tweepy 객체 생성

keyword="삼성전자"
search = []

f = io.open('./samsung_test.txt',"w",encoding="utf-8")
cnt=1
while (cnt<=100):
    tweets = api.search(keyword)  #트위터 키워드 검색
    for tweet in tweets:
        f.write(tweet.text +'\n')   #트위터 내용 가져와서 파일에 쓰기
        search.append(tweet.text)
    cnt+=1
print(len(search))
f.close()

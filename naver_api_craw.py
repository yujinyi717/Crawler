# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json


client_id = "id"
client_secret = "pw"
encText = urllib.parse.quote("부산 중구")

def create_url(start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start) # json 결과
#     url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText + "&display=100" + "&start=" + str(start)# xml 결과
    return url
url = create_url(1)
   
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

for i in range(1,1001,100):
    url = create_url(i)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        results = response_body.decode('utf-8')
        items = json.loads(results)['items']
        for item in items:
            f = open('크롤링.text','a',encoding='utf-8')
            title = item['title']
            description = item['description']
            date = item["postdate"]
            
            title = title.replace('<b>','')
            title = title.replace('</b>','')
            description = description.replace('<b>','')
            description = description.replace('</b>','')
            description = description.replace('...','')
            
            f.write(title + '\n')
            f.write(description + '\n')
            f.write(date + '\n')
            f.close()
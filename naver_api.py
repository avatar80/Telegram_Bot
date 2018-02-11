import urllib.request

client_id = 'g8mcX6g0mg4EQ957cooq'
client_secret = 'WLNIzHjPwX'

search_text = urllib.parse.quote('닌텐도스위치')

# url = "https://openapi.naver.com/v1/search/book.json?query=" + search_text # json 결과
url = "https://openapi.naver.com/v1/search/shop.json?query=" + search_text + "&display=10"

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
# https://search.shopping.naver.com/search/all.nhn?where=all&query=%EB%8B%8C%ED%85%90%EB%8F%84+%EC%8A%A4%EC%9C%84%EC%B9%98
#https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%8B%8C%ED%85%90%EB%8F%84%20%EC%8A%A4%EC%9C%84%EC%B9%98&pagingIndex=1&pagingSize=40&viewType=list&sort=review&query=%EB%8B%8C%ED%85%90%EB%8F%84%20%EC%8A%A4%EC%9C%84%EC%B9%98
# _model_list _itemSection

import requests
from bs4 import BeautifulSoup


def search_price_with_review(product_name):
    url = 'https://search.shopping.naver.com/search/all.nhn'
    params = {
        'query': product_name,
        'where': 'all',
        'sort': 'review',
    }
    response = requests.get(url, params=params)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    item_list = soup.select('.info')
    for values in item_list:
        title = values.find(class_='tit').text.strip()
        price = values.find(class_='num').text.strip()
        print(title, price)






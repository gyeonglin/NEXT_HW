import requests
from bs4 import BeautifulSoup
import csv

file = open('notebook1.csv', mode='w', newline='', encoding="utf-8-sig")
writer = csv.writer(file)
writer.writerow(["title", "price", "detail"])


final_result=[]

# 우리가 정보를 얻고 싶어 하는 URL

for page in range(30) :
    NOTEBOOK_URL = f'https://search.shopping.naver.com/search/all?pagingIndex={page}&pagingSize=80&query=노트북'
    # get 요청을 통해 해당 페이지 정보를 저장
    notebook_html = requests.get(NOTEBOOK_URL)
    # bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
    notebook_soup = BeautifulSoup(notebook_html.text,"html.parser")
    notebook_list_box = notebook_soup.find('ul', {'class':'list_basis'})
    notebook_list = notebook_list_box.find_all('li', {'class':'basicList_item__2XT81'})


    for notebook in notebook_list :
        title = notebook.find('div', {'class':'basicList_title__3P9Q7'}).find('a').text
        price = notebook.find('span', {'class':'price_num__2WUXn'}).text
        detail = notebook.find('div', {'class':'basicList_detail_box__3ta3h'}).find_all('a', {'class':'basicList_detail__27Krk'})

        detail_list=[]

        for detail_item in detail :
            detail_list.append(detail_item.text)

        result = {
        'title' : title,
        'price' : price,
        'detail' : detail_list
        }


        final_result.append(result)
        
print(final_result)

for result in final_result :
    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['detail'])

    writer.writerow(row)




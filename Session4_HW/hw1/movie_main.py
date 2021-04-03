import requests
from bs4 import BeautifulSoup
from movie_notebook import extract_info
from urllib.request import urlretrieve
import csv

file = open('Newmovie.csv', mode='w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(['img', 'title', 'score', 'date', 'director', 'actor'])

MOVIE_URL = f"https://movie.naver.com/movie/running/current.nhn"
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text, "html.parser")
movie_list_box = movie_soup.find('ul', {'class':'lst_detail_t1'})
movie_list = movie_list_box.find_all('dl', {'class':'lst_dsc'})
movie_img_list = movie_list_box.find_all('div', {'class':'thumb'})

final_result = extract_info(movie_img_list, movie_list)

for result in final_result :
    row = []
    row.append(result['img'])
    row.append(result['title'])
    row.append(result['score'])
    row.append(result['date'])
    row.append(result['director'])
    row.append(result['actor'])


    writer.writerow(row)



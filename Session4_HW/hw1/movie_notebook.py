def extract_info(movie_img_list, movie_list) :
    final_result = []

    for movie_img, movie_item in zip(movie_img_list, movie_list) :
        img_src = movie_img.find('img')['src']
        title = movie_item.find('dt', {'class':'tit'}).find('a').text
        score = movie_item.find('div', {'class':'star_t1'}).find('span', {'class':'num'}).text

        text_info = movie_item.find('dl', {'class':'info_txt1'}).find_all('dd')
        if len(text_info)>=3 :
            date = text_info[0].text.split('|')[2].strip()
            director = text_info[1].text.strip().replace('\t','').replace('\r','').replace('\n','')
            actor = text_info[2].text.strip().replace('\t','').replace('\r','').replace('\n','')
        else :
            date = text_info[0].text.split('|')[2].strip()
            director = text_info[1].text.strip()
            actor = None

        result = {
            'img' : img_src,
            'title' : title,
            'score' : score,
            'date' : date,
            'director' : director,
            'actor' : actor
        }

        final_result.append(result)
    return final_result


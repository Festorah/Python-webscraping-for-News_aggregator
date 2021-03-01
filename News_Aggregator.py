# Importing required dependencies

from bs4 import BeautifulSoup
import requests


# For Sports news (skysports)
url_sport = 'https://www.skysports.com/football/news'
source = requests.get(url_sport).text
soup = BeautifulSoup(source, 'lxml')
articles_sport = soup.find_all('div', class_='news-list__item news-list__item--show-thumb-bp30')
count = 1
headline_sport_container = list()
newslink_sport_container = list()
img_src_sport_container = list()
time_sport_container = list()
summary_sport_container = list()

for article_sport in articles_sport:
    
#     Headline
    headline_sport_wrapper = article_sport.find('div', class_='news-list__body')
    headline = headline_sport_wrapper.h4.a.text.strip(" ")
    headline_sport_container.append(headline)

    
#     newslink
    newslink_sport = headline_sport_wrapper.h4.a['href']
    newslink_sport_container.append(newslink_sport)


#     Image
    img_sport_src = article_sport.a.img['data-src'].split('?')[0]
    img_src_sport_container.append(img_sport_src)


#     Time
    time_sport_wrapper = article_sport.find('div', class_='label')
    time_sport = time_sport_wrapper.span.text
    time_sport_container.append(time_sport)


#     Summary
    summary_sport = headline_sport_wrapper.p.text
    summary_sport_container.append(summary_sport)
    
    # Printing the features in each iteration

    # print(count)
    # print(f'Headline','\n',headline)
    # print(f'News Link','\n',newslink)
    # print(f'Image Source','\n',img_src)
    # print(f'Time Posted','\n',time)
    # print(f'Summary','\n',summary)
    # print('\n')

    count += 1



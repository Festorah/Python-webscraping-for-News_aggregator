from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.forbesafrica.com/category/entrepreneurs/').text
soup = BeautifulSoup(source, 'lxml')
articles = soup.find_all('li', class_='mvp-blog-story-wrap left relative infinite-post')
counter = 1
for news in articles:
#     link
    link = news.a['href']
    
#     headline
    headline = news.a.h2.text
    
#     Image Source
    img_src = news.a.img['src']
    
    print(counter)
    print(headline)
    print(link)
    print(img_src)
    print()
    counter += 1
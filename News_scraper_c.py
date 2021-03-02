from bs4 import BeautifulSoup
import requests


url = 'https://guardian.ng/category/politics/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
headlines_wrapper = soup.find_all('div', class_='row row-3')
counter = 3


for headline in headlines_wrapper:
    link_wrapper = headline.find_all('div', class_='cell')
    
    for link_wrap in link_wrapper:
        
#         for the link
        link = link_wrap.a['href']
        
#         for the Headline
        headline = link_wrap.a.span
        img_src = link_wrap.find('div', class_='image')
        
#         For first five irrelevant tags (from the website)
        if counter <= 5:
            pass
        else:
            if counter == 6:
                print(headline.text)
                print(link)
                imgj = img_src.img['data-lazy-src']
                print(imgj)
        counter += 1

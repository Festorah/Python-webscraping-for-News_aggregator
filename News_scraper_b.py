from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.legit.ng/').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('section', class_='l-article-column l-hero-section__column')

news = soup.find_all('article')
counter = 1

for sno, article in enumerate(news, counter):

	# headline
    headline = article.span.text
    print(headline)

	# link
    link = article.a['href']
    print(link)

    # time
    time = article.time.text.strip('\n  ')
    print(time)
    print()
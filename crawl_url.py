# crawl the data from differet webs
import requests
from bs4 import BeautifulSoup

# get the html format of web
def getHTMLText(url):
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        res.encoding = res.apparent_encoding

        return res.text
    except:
        return 'ERROR'

#get the hyperlink from url
def main(url):

    html = getHTMLText(url)

    soup = BeautifulSoup(html, 'html.parser')

    a_lables = soup.find_all('a', attrs={'href': True})

    return a_lables

# the hyperlinks may be not all satisfy the requirement, so personal selection is necessary


# the hyperlink crawling for financial
financial_url = 'https://www.finweb.com/recent-articles.html'
financial_labels = main(financial_url)
financial_file = open('.\data\\financial_url.txt', 'w+', encoding='UTF-8')
for a in financial_labels:
    strl = 'https://www.finweb.com/' + a.get('href') + '\n'
    if 'index.html' not in strl:
        if 'comhttps' not in strl:
                financial_file.write(strl)
financial_file.close()



# the hyperlink crawling for tech
tech_url = 'https://mashable.com/articles'
tech_file = open('.\data\\tech_url.txt', 'w+', encoding='UTF-8')
# crawl the hyperlink from page2 to page9
for i in range(2, 10):
    temp_url = 'https://mashable.com/articles' + '?page=' + str(i)
    tech_labels = main(temp_url)
    print(tech_labels)
    for a in tech_labels:
        strl = 'https://mashable.com' + a.get('href') + '\n'
        print(strl)
        if 'com/article/' in strl:
            tech_file.write(strl)
tech_file.close()



# the hyperlink crawling for energy
energy_url = 'https://www.iea.org/news'
energy_file = open('.\data\\energy_url.txt', 'w+', encoding='UTF-8')
# crawl the hyperlink from page1 to page9
for i in range(1, 10):
    temp_url = energy_url + '?page=' + str(i)
    health_labels = main(temp_url)
    for a in health_labels:
        strl = 'https://www.iea.org' + a.get('href') + '\n'
        if 'org/news/' in strl:
            energy_file.write(strl)
energy_file.close()



# the hyperlink crawling for health
health_url = 'https://www.who.int/news-room/headlines'
health_file = open('.\data\\health_url.txt', 'w+', encoding='UTF-8')
# crawl the hyperlink from page1 to page9
for i in range(1, 10):
    temp_url = health_url + '/' + str(i)
    health_labels = main(temp_url)
    for a in health_labels:
        strl = 'https://www.who.int' + a.get('href') + '\n'
        if 'int/news/item/' in strl:
            health_file.write(strl)
health_file.close()



# the hyperlink crawling for Educational, Scientific and Cultural
culture_url = 'https://www.unesco.org/en/newsroom/press-release'
culture_file = open('.\data\\culture_url.txt', 'w+', encoding='UTF-8')
# crawl the hyperlink from page1 to page9
for i in range(1,16):
    temp_url = culture_url + '?page=' + str(i-1)
    culture_labels = main(temp_url)
    for a in culture_labels:
        strl = 'https://www.unesco.org' + a.get('href') + '\n'
        if 'en/articles/' in strl:
            culture_file.write(strl)
culture_file.close()

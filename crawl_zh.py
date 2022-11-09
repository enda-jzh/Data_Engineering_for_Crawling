# crawl articles in chinese
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



health_url = 'http://www.xinhuanet.com/health/index.html'
health_labels = main(health_url)
health_file = open('.\data_zh\health_url_zh.txt', 'w+', encoding='UTF-8')
for a in health_labels:
    strl = 'https://www.xinhuanet.com' + a.get('href') + '\n'
    if 'com/health/2' in strl:
        health_file.write(strl)
health_file.close()



financial_url = 'http://www.xinhuanet.com/fortunepro/index.html'
financial_labels = main(financial_url)
financial_file = open('.\data_zh\\financial_url_zh.txt', 'w+', encoding='UTF-8')
for a in financial_labels:
    strl = a.get('href') + '\n'
    if 'cn/fortune/' in strl:
        financial_file.write(strl)
financial_file.close()


tech_url = 'http://www.xinhuanet.com/techpro/'
tech_labels = main(tech_url)
tech_file = open('.\data_zh\\tech_url_zh.txt', 'w+', encoding='UTF-8')
for a in tech_labels:
    strl = a.get('href') + '\n'
    if '/techpro/2' in strl:
        strl = 'http://www.xinhuanet.com' + a.get('href') + '\n'
        tech_file.write(strl)
    elif 'cn/science/2' in strl:
        tech_file.write(strl)
tech_file.close()


culture_url = 'http://www.xinhuanet.com/culturepro/'
culture_labels = main(culture_url)
culture_file = open('.\data_zh\\culture_url_zh.txt', 'w+', encoding='UTF-8')
for a in culture_labels:
    strl = a.get('href') + '\n'
    if 'cn/culturepro/2' in strl:
        culture_file.write(strl)
    elif '/culturepro/2' in strl:
        strl = 'http://www.xinhuanet.com' + a.get('href') + '\n'
        culture_file.write(strl)
culture_file.close()


sports_url = 'http://sports.news.cn/'
sports_labels = main(sports_url)
sports_file = open('.\data_zh\\sports_url_zh.txt', 'w+', encoding='UTF-8')
for a in sports_labels:
    strl = a.get('href') + '\n'
    if 'cn/c/2' in strl:
        sports_file.write(strl)
sports_file.close()

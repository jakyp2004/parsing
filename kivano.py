import csv
from cvs import CSV
from bs4 import BeautifulSoup
import requests
import kivano

KIVANO= 'minfin.kivano' 
HOST = 'https://www.kivano.kg/planshety'   
URL = 'https://www.kivano.kg/?gclid=EAIaIQobChMI_re19pu88QIVE2EYCh322QYOEAAYASAAEgJiMPD_BwE'
HEADERS = {
    'Accept': '*/*', 
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
    }

def get_html(url, params=''):
    r = requests.get(URL , headers=HEADERS, verify=False, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div' , class_='news')
    news_list = []

    for item in items:
        news_list.append({
            'date' : item.find('div' , class_= 'news_date').get_text(strip=True),
            'title' : item.find('div', class_ = 'news_name').get_text(strip=True),
            'link' : HOST + item.find('div', class_ = 'news_name').find('a').get('href'),
        })

    return news_list
    


def news_save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['день публикации' , 'новость' , 'ссылка'])

        for item in items:
            writer.writerow([item['date'], item['title'], item['link']])

def parcer():
    PAGENATOR = input("ведите каличество страниц: ")
    PAGENATOR = int(PAGENATOR.strip())
    html = get_html(URL)
    if html.status_code == 200:
        news_list = []
        for page in range (1, PAGENATOR):
            print(f'страница {page} готова')
            html = get_html(URL , params={'page' :page})
            news_list.extend(get_content(html.text)) 
        news_save(news_list, CSV)
        print('Парсинг готов')
    else :
        print('Error')


parcer()            

               

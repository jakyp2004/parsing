
from bs4 import BeautifulSoup
import requests
def save():
    with open('sulpak_comps.txt' , 'a') as file:
        file.writelines(f"название: {comp['title']}, цена: {comp['price']}, ссылка : {comp['link']}")



def parce():
    URL = 'https://www.sulpak.kg/f/noutbuki/'
    HEADERS = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'
        }

    response = requests.get(URL, headers = HEADERS, verify = False)
    soup = BeautifulSoup(response.content , 'html.parser')
    items = soup.findAll('div' , class_ = 'goods-tiles')
    comps = []

    for item in items:
        try:
            comps.append({
            'title' : item.find('h3' , class_ = 'title').get_text(strip=True),
            'price' : item.find('div' , class_= 'price').get_text(strip=True),
            'link'  : URL + item.find('div', class_ = 'product-container-right-side').find('a').get('href'),
        })
        except:
            pass
    global comp      
    for comp in comps:
        print(f"название : {comp['title']}, цена : {comp['price']},ссылка : {comp['link']}")
        save()

        
               





parce()
import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
  response = requests.get(url)
  soup = BS(response.text, 'lxml')
  models = [i for i in soup.select('a[href^="/details/"]')]

  for auto in models:
    name = auto.find('h2', class_ = 'name').text.strip()
    price = auto.find('p', class_ = 'price').find('strong').text
    img = auto.find('div', class_ = 'thumb-item-carousel').find('img', class_ = 'lazy-image').get('data-src')
    opi1 = auto.find('p', class_ = 'year-miles').text.strip()
    opi2 = auto.find('p', class_ = 'body-type').text.strip()
    opi3 = auto.find('p', class_ = 'volume').text.strip()
    opisan = opi1 + ' ' + opi2 + ' ' + opi3

    write_csv({'title': name, 'price': price, 'image': img, 'description': opisan})

def write_csv(data):
  with open('mashina.csv', 'a') as file:
    names = ['title', 'price', 'image', 'description']
    write = csv.DictWriter(file, delimiter=',', fieldnames=names)
    write.writerow(data)
  
url = "https://www.mashina.kg/commercialsearch/all/?page=1"
for i in url:
  if 'page=1' in i:
    get_html(url)
  else:
    url2 = 'https://www.mashina.kg/commercialsearch/all/'
    i = 1
    url2 += '?page=' + str(i)
    i += 1
    get_html(url2)
    if i == 167:
      break
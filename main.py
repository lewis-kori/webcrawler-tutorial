import requests
import json
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

base_url = "http://books.toscrape.com/"

r = requests.get(base_url,headers=header)

if r.status_code == 200:
  soup = BeautifulSoup(r.text, 'html.parser')
  books = soup.find_all('li',attrs={"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
  result=[]
  for book in books:
    title=book.find('h3').text
    link=base_url +book.find('a')['href']
    stars = str(len(book.find_all('i',attrs=  {"class":"icon-star"}))) + " out of 5"
    price="$"+book.find('p',attrs={'class':'price_color'}).text[2:]
    picture = base_url + book.find('img')['src']
    single ={'title':title,'stars':stars,'price':price,'link':link,'picture':picture}
    result.append(single)
    with open('books.json','w') as f:
      json.dump(result,f,indent=4)
else:
  print(r.status_code)

from requests import get
from bs4 import BeautifulSoup as bs

data = {}
name = []
price = []

url = 'https://www.amazon.com.br/gp/aw/s/ref=nb_sb_noss?k=iphone'
request = get(url)
page = bs(request.content, 'html.parser')
boxes = page.find_all('div', {'class' : 'a-section a-spacing-medium'})

for box in boxes:
	n = box.find('span', {'class' : 'a-size-base-plus a-color-base a-text-normal'}).text
	name.append(n)
	p = box.find_all('span', {'class' : 'a-price-whole'})
	if len(p) > 0:
		price.append(p[0].text)
	else:
		price.append('None')
data['name'] = name
data['price'] = price

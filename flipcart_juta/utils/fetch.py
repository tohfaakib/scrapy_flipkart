import re
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_shoe_template_json_date(title, product_url, variants):
	
	return {
		'title': title,
		'product_url':product_url,
		'variants':variants
	}

def get_shoe_variant_json_data(url):
	html = urlopen(url)
	data = html.read()
	soup_attr = BeautifulSoup(data, "html.parser")
	title = soup_attr.find('span', class_='_35KyD6').text
	stock_price = soup_attr.find('div', class_='_3auQ3N _1POkHg').text
	selling_price = soup_attr.find('div', class_='_1vC4OE _3qQ9m1').text
	images = soup_attr.find_all('div', class_='_2_AcLJ _3_yGjX')
	list_images = []
	for img in images:
		style = img['style']
		list_images.append(str(re.findall('url\((.*?)\)', style)[0]).replace('128/128/', ''))
	
	size = soup_attr.find('a', class_='_1TJldG _3c2Xi9 _2I_hq9 _2UBURg').text
	color = soup_attr.find_all('a', class_="_3c2Xi9")[0].find_next_sibling('div').text
	
	return {
		'title': title,
		'stock_price': stock_price,
		'selling_price': selling_price,
		'images': list_images,
		'color': color,
		'size': size
	}
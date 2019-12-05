#!/usr/local/bin/python3

from bs4 import BeautifulSoup
from termcolor import colored
import requests
import re
import json
#import time

#grab user search string
product = input("What product would you like to search for? ")
#product = "tomato sauce"
print(f"Product was: {product}")
#time.sleep(10)

#woolworths needs specific headers - defining them below
woolworthsHeaders = {
	'Accept': 'application/json, text/plain, */*',
	'Referer': 'https://www.woolworths.co.za/cat?Ntt=tomato%20sauce&Dy=1'
}

#import the data
pnp = requests.get(f"https://www.pnp.co.za/pnpstorefront/pnp/en/search/?text={product}")
woolies = requests.get(f"https://www.woolworths.co.za/server/searchCategory?pageURL=%2Fcat&Ntt={product}&Dy=1", headers=woolworthsHeaders)

#print the HTTP response
#print(f"{woolies.text}")
myWoolworthsJSON = json.loads(woolies.text)
print(f"{myWoolworthsJSON}")


#load the data into BS4
soup = BeautifulSoup(pnp.text, 'html.parser')
soup2 = BeautifulSoup(woolies.text, 'html.parser')
#print(soup2)
exit()

# get data simply by looking for each h4 header (which contains the username)
data = []
for div in soup.find_all('div', { 'class': 'item-name'}):
	data.append(div.text)

# get the comments of each user by looking for a div with class bbWrapper
data2 = []
for div in soup.find_all('div', { 'class': 'currentPrice' }):
	#remove all data with <div> or </div> or </span> or with spaces
	div = re.sub(r'(^<div.*>|</div.*>|</span>|\s)', '', str(div))
	#replace <span> with a . (pnps website has a span element separating rands and cents!)
	div = re.sub(r'<span>', '.', str(div))
	data2.append(div)

myCount=0
with open(f'./pnpPrices.json', 'w+') as f:
	myProductData = []
	#myProductData['picknpay'] = []
	for product in data:
		#print(colored(f"Product: {product}", 'red'))
		#print(colored(f"Price: {data2[myCount]}", 'green'))
		content = {
			'product': product,
			'price': data2[myCount]
			}
		print(content)
		#myData = str(content).","
		#print(myData)
		myProductData.append(content)
		myCount+=1
		#json.dump(content, f)
	json.dump(myProductData, f)



############# Woolies section ##############

# get data simply by looking for each h4 header (which contains the username)
data = []
for a in soup2.find_all('a', { 'class': 'range--title'}):
	data.append(a.text)
	#print(f"A RECORD: {a}")

# get the comments of each user by looking for a div with class bbWrapper
data2 = []
for strong in soup2.find_all('strong', { 'class': 'price' }):
	#remove all data with <div> or </div> or </span> or with spaces
	#strong = re.sub(r'(^<div.*>|</div.*>|</span>|\s)', '', str(div))
	#replace <span> with a . (pnps website has a span element separating rands and cents!)
	#div = re.sub(r'<span>', '.', str(div))
	data2.append(strong.text)
	#print("FOUND STRONG")

myCount=0
with open(f'./wooliesPrices.json', 'w+') as f:
	myProductData = []
	#myProductData['picknpay'] = []
	for product in data:
		#print(colored(f"Product: {product}", 'red'))
		#print(colored(f"Price: {data2[myCount]}", 'green'))
		content = {
			'product': product,
			'price': data2[myCount]
			}
		#print(content)
		#myData = str(content).","
		#print(myData)
		myProductData.append(content)
		myCount+=1
		#json.dump(content, f)
	json.dump(myProductData, f)

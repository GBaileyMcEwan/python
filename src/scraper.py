#!/usr/bin/python3

from bs4 import BeautifulSoup
from termcolor import colored
import requests
import re

#import the data
data = requests.get("https://mybroadband.co.za/forum/threads/prepare-for-bitcoin-mayhem.1058511/")

#print the HTTP response
#print(f"{data.text}")

#load the data into BS4
soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for each h4 header (which contains the username)
data = []
for h4 in soup.find_all('h4'):
	values = [a.text for a in h4.find_all('a')]
	data.append(values)

# get the comments of each user by looking for a div with class bbWrapper
data2 = []
for div in soup.find_all('div', { 'class': 'bbWrapper' }):
	#print(f"{div.text}")
	#values = [div.text for div in article.find_all('div', { 'class': 'bbWrapper' })
	data2.append(div.text)

myCount=0
print(data2[myCount])
for username in data:
	print colored(f"Username: {username} said", 'red')
        print(f"\nComment: {data2[myCount]}")
        print(f"\nCount: {myCount}")
	myCount+=1


	

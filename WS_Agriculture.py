import requests
from bs4 import BeautifulSoup
import re

url = "https://www.agroinfomedia.com/"

response = requests.get(url)

soup= BeautifulSoup(response.text,"html.parser")

names=soup.find('strong').get_text()

print(names)
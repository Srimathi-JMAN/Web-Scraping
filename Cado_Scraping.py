import requests
from bs4 import BeautifulSoup

session=requests.Session()

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36 Edg/132.0.0.0'
}

session.headers.update(headers)

url = 'https://cado.eservices.gov.nl.ca/Company/CompanyNameNumberSearch.aspx'
response = session.get(url)
soup=BeautifulSoup(response.text,'html.parser')

viewState = soup.find('input',{'id':"__VIEWSTATE"}).get('value')
viewStateGenerator = soup.find('input',{'id':'__VIEWSTATEGENERATOR'}.get('value'))
print(viewStateGenerator)
import time
import requests
from bs4 import BeautifulSoup

session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36 Edg/132.0.0.0',
}

session.headers.update(headers)

URL = 'https://cado.eservices.gov.nl.ca/Company/CompanyNameNumberSearch.aspx'

# First GET request
response = session.get(URL)
time.sleep(2)  # Short delay

# Parse response
soup = BeautifulSoup(response.text, 'html.parser')

# Extract hidden form fields
payload = {
    '__VIEWSTATE': soup.find('input', {'id': "__VIEWSTATE"}).get('value'),
    '__VIEWSTATEGENERATOR': soup.find('input', {'id': '__VIEWSTATEGENERATOR'}).get('value'),
    '__EVENTVALIDATION': soup.find('input', {'id': '__EVENTVALIDATION'}).get('value'),
    'txtNameKeywords1': 'AAA',  # Search query
    'btnSearch': 'Search'  # Some forms require submitting the button too
}

# Submit POST request with form data
res = session.get(URL, data=payload)
time.sleep(2)  # Short delay

# Parse the new response
soup = BeautifulSoup(res.text, 'html.parser')

# Find all <td> tags with width="430"
company_boxes = soup.findAll('td', {'width': '430'})

# Extract company names from the <a> tags
for company_box in company_boxes:
    company_link = company_box.find('a')  # Find <a> inside <td>
    if company_link:
        company_name = company_link.text.strip()  # Extract text
        print(company_name)  # Output: *AAA* MarketChina Inc.

print(company_boxes)

# import time
# import requests
# from bs4 import BeautifulSoup


# session=requests.Session()

# headers = {
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36 Edg/132.0.0.0',
# }

# session.headers.update(headers)

# URL = 'https://cado.eservices.gov.nl.ca/Company/CompanyNameNumberSearch.aspx'

# response = session.get(URL)

# time.sleep(2)

# soup=BeautifulSoup(response.text,'html.parser')

# payload = {
#     '__VIEWSTATE' : soup.find('input',{'id':"__VIEWSTATE"}).get('value'),
#     '__VIEWSTATEGENERATOR' : soup.find('input',{'id':'__VIEWSTATEGENERATOR'}).get('value'),
#     '__EVENTVALIDATION': soup.find('input',{'id':'__EVENTVALIDATION'}).get('value'),
#     'txtNameKeywords1': 'aa',
# }

# res=session.post(URL,data=payload)

# soup=BeautifulSoup(res.text,'html.parser')

# company_boxes = soup.find('td',{'width':'430'})


# print(company_boxes)

# #rptCompanyNameSearchResults__ctl1_lbtCompanyNumber
# //*[@id="rptCompanyNameSearchResults__ctl1_lbtCompanyNumber"]
# /html/body/form/table[3]/tbody/tr[6]/td/table/tbody/tr/td/table/tbody/tr[2]/td[1]/a

import requests

from bs4 import BeautifulSoup

import pandas as pd

baseUrl = "https://www.yellowpages-uae.com"
total=67
data=[]

def getName(item: BeautifulSoup):
    try:
        name=item.find('h2', attrs={"itemprop":"name", "id": "name"}).text.replace("\n","")
    except:
        name='None'

    return name

def getAddress(item: BeautifulSoup):
    try:
        address=item.find('span', attrs={"itemprop":"streetAddress"}).text
    except:
        address='None'
        
    return address

def getPostalCode(item: BeautifulSoup):
    try:
        postalCode=item.find('span', attrs={"itemprop":"postalCode"}).text
    except:
        postalCode='None'
        
    return postalCode

def getCity(item: BeautifulSoup):
    try:
        locality=item.find('strong', attrs={"itemprop":"addressLocality"}).text
        region=item.find('strong', attrs={"itemprop":"addressRegion"}).text

        city=locality + "," + region
    except:
        city='None'
        
    return city

def getPhone(item: BeautifulSoup):
    try:
        phoneLink = item.find('a', attrs={"title":"Phone"})
        phone=phoneLink.find('span', attrs={"itemprop":"telephone"}).text
    except:
        phone='None'
        
    return phone

def getMobile(item: BeautifulSoup):
    try:
        mobileLink = item.find('a', attrs={"title":"Mobile"})
        mobile = mobileLink.find('span', attrs={"itemprop":"telephone"}).text
    except:
        mobile='None'
        
    return mobile

def getBussinessPage(item: BeautifulSoup):
    try:
        titleDiv = item.find('div', attrs={"class":"row title-row"})
        business_page = titleDiv.find('a').get('href')
    except:
        business_page='None'
        
    return baseUrl + business_page

def getLogo(item: BeautifulSoup):
    try:
        logoDiv = item.find('div', attrs={"class":"logobox"})
        logo = logoDiv.find('img').get('data-src')
    except:
        logo='None'
        
    return  logo

for i in range(1, total):
    

    url=f'https://www.yellowpages-uae.com/uae/restaurant-{i}.html'
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

    r=requests.get(url, header)
    soup=BeautifulSoup(r.content, 'html.parser')

    articles=soup.findAll('div', attrs={"itemtype":"https://www.schema.org/LocalBusiness"})
    
    for item in articles:
        name = getName(item)
        address = getAddress(item)
        city = getCity(item)
        postalCode = getPostalCode(item)
        phone = getPhone(item)
        mobile = getMobile(item)
        bussinessPage = getBussinessPage(item)
        logo = getLogo(item)

        data.append([name, address, city, postalCode, "+97" + phone, "+97" + mobile, bussinessPage, logo])

df=pd.DataFrame(data, columns=['name','address','city','postalCode','phone','mobile','business_page','logo'])

df.to_csv('data.csv', index_label='index')

print("Data saved in data.csv")
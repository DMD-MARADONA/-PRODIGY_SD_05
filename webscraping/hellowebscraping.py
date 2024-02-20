#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# In[12]:


#Connect to website
URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=&customizationToken=MC_Assembly_1%23B0752XJYNL'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content,"html.parser")

soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id='productTitle').get_text()

soup3 = BeautifulSoup(soup2.prettify(),"html.parser")

div = soup3.find_all('div',class_='')

noRatings = soup2.find(id='acrCustomerReviewText').get_text()

print(title)
print(noRatings)
print(div)


# In[ ]:


#Cleaning data
ratingcount = noRatings.strip()[:2]
title = title.strip()
print(title)
print(ratingcount)


# In[ ]:


#Getting todays date
import datetime
today = datetime.date.today()
print(today)


# In[ ]:


#Creating a csv file
import csv

header = ['Tittle','Price','Date']
listdata = [title,ratingcount,today]

with open('AmazoneFirstWebScrapp.csv','w', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(listdata)


# In[ ]:


#Reading csv file
import pandas as pd
df = pd.read_csv(r'C:\Users\07SAW\AmazoneFirstWebScrapp.csv')
print(df)


# In[ ]:


#Appending data
with open('AmazoneFirstWebScrapp.csv','a+', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(listdata)


# In[ ]:


def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=&customizationToken=MC_Assembly_1%23B0752XJYNL'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content,"html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

    title = soup2.find(id='productTitle').get_text()

    noRatings = soup2.find(id='acrCustomerReviewText').get_text()
    
    ratingcount = noRatings.strip()[:2]
    
    title = title.strip()
    
    import datetime
    today = datetime.date.today()
    
    import csv

    header = ['Tittle','Price','Date']
    listdata = [title,ratingcount,today]
    
    with open('AmazoneFirstWebScrapp.csv','a+', newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(listdata)


# In[ ]:


#Check price timeously
while(True):
    check_price()
    time.sleep(43200)


# In[ ]:


#Reading csv file
import pandas as pd
df = pd.read_csv(r'C:\Users\07SAW\AmazoneFirstWebScrapp.csv')
print(df)


# In[ ]:





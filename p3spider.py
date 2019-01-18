#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml


result=requests.get('https://www.ptt.cc/bbs/joke/M.1547741976.A.4AC.html')
soup=BeautifulSoup(result.text,'lxml')
title=soup.find_all('div') 

for i in title:
    if i.find('span','article-meta-tag'):
        result2=i.find('span','article-meta-tag').text
        print(result2)
    if i.find('span','article-meta-value'):
        result5=i.find('span','article-meta-value').text
        print(result5)
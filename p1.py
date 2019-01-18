#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import time




urls = [ "http://www.google.com/a.txt",
          "http://www.google.com.tw/a.txt",
          "http://www.google.com/download/c.jpg",
          "http://www.google.co.jp/a.txt",
          "http://www.google.com/b.txt",
          "https://facebook.com/movie/b.txt",
          "http://yahoo.com/123/000/c.jpg",
          "http://gliacloud.com/haha.png",
]

a=[]
b=[]
c=[]
long=len(urls)
for i in range(0,long):
    
    result=urls[i].split('//')
    result2=result[1].split('/')
    if result2[1]=="a.txt":
       a.append(result2[1])
    if result2[1]=="b.txt":
       b.append(result2[1])
    if result2[1]=="c.jpg":
       c.append(result2[1])
   
print("a.txt",len(a))
print("b.txt",len(b))
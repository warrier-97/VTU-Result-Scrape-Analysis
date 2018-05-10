# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:41:58 2018

@author: ADITYA
"""

import requests,csv,itertools
from bs4 import BeautifulSoup

url = "http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php"
lis=list()


for i in itertools.chain(range(1,57),[400]):
    x=list()
    if i<=9:
        usn='1AT15IS00'+str(i)
    elif i==400:
        usn='1AT16IS'+str(i)
    else:
        usn='1AT15IS0'+str(i)
    try:
        r = requests.post(url,data = {'lns':usn})
        soup = BeautifulSoup(r.text, "html.parser")
        det=soup.find("div",{"class","col-md-12 table-responsive"})
        n=det.findChildren("td")
        usn = n[1]
        name = n[3]
        print(name)
        if(name.contents[1]==" "):continue
        x.extend((usn.contents[1],name.contents[1]))
        marks=soup.find_all("div",{"class","divTableCell"})

        for j in range(6,len(marks)-5):
            var = marks[j]
            x.append(var.contents[0])
        
        l=["Subject Code","Subject Name","Internal Marks","External Marks","Total","Result"]
        for i in l:
            if i in x:
                num=x.count(i)
                for j in range(num):
                    x.remove(i)
                    
        lis.append(x)
    except:
        continue

#headings=["USN","Name",""]

with open("res_dump.csv","w",newline='') as file:
    w=csv.writer(file)
    w.writerows(lis)
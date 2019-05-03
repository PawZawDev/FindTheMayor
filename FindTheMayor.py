"""
Written by Pawel Zawierucha
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

wiki_url=r"https://en.wikipedia.org/wiki/"
while(True):
    try:
        city=str(input("Tell me the city: "))
        final_url=wiki_url+city

        page=urlopen(final_url)
        soup=BeautifulSoup(page,"html.parser")
        whole_table=soup.find("table",attrs={"class":"infobox"})
        
        content=whole_table.text.strip()
    except:
        print("Sorry, can't find anything, please try again\n")
        continue

    check_mayor=re.search(r"Mayor",content)
    #the box after mayor (the one we dont want)
    check_area=re.search(r"Area",content)

    if(check_mayor) and (check_area):
        prez=content[check_mayor.end():check_area.start()]
        print("The mayor of "+city+" is "+prez)
        break
    else:
        print("Sorry, can't find anything, please try again\n")
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
        city=city.lower()
        if (city=="quit"):
            break
        elif (city=="jerusalem"):
            print("well, this city breaks the whole thing")
            print("Please search for something else")
            continue
        final_url=wiki_url+city

        page=urlopen(final_url)
        soup=BeautifulSoup(page,"html.parser")
        whole_table=soup.find("table",attrs={"class":"infobox"})
        
        content=whole_table.text.strip()
    except:
        print("Sorry, can't find anything, please try again\n")
        continue
    
    #mayor_pattern=r"[^A-Za-z]Mayor[A-Za-z ()]*"
    mayor_pattern=r"[^A-Za-z]Mayor"
    dot=r"•"
    check_mayor=re.search(mayor_pattern,content)
    hyperlink_pattern=r"\[[1-9]*\]"

    
    #the box after mayor (the one we dont want)
    # print (content)
    
    check_area=re.search(r"Area",content)
    if(check_mayor) and (check_area):
        #print(content)
        content=content[check_mayor.end():check_area.start()]
        check_dot=re.search(dot,content)
        if (check_dot):
            content=content[:check_dot.start()]
        check_hyper=re.match(hyperlink_pattern,content)
        if(check_hyper):
            content=content[check_hyper.end():]
        check_hyper=re.search(hyperlink_pattern,content)
        if (check_hyper):
            content=content[:check_hyper.start()]

        # while(1):
        #     #check_hyper=re.search(hyperlink_pattern,content)
        #     content=content.replace(hyperlink_pattern,"")
        #content=content.replace(hyperlink_pattern,"")


        # prez=content[check_mayor.start():check_mayor.end()]
        # check_area=re.search(r"Area",prez)
        # if(check_area):
        #     prez=prez[:check_area.start()]
        # check_mayor_start=re.match(r"[^A-Za-z]?Mayor[^A-Za-z]?",prez)
        # if(check_mayor_start):
        #     prez=prez[check_mayor_start.end():]


        # print(check_mayor.group())
        # print(check_mayor.start())
        # print(check_mayor.end())

        prez=content
        print("The mayor of "+city+" is "+prez)
        break
    else:
        print("Sorry, can't find anything, please try again\n")
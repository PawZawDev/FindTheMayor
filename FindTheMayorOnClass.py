"""
Written by Pawel Zawierucha
Using BeautifulSoup to scrape data from wikipedia
Using PyQt5 for GUI

This is the logic part
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

    
class FindTheMayor:
    wiki_url=r"https://en.wikipedia.org/wiki/"
    def __init__(self):
        # self.do_magic()
        self.last_city="Neverland"
        pass

    def do_magic(self):
        
        while(True):
            try:
                self.last_city=str(input("Tell me the city: "))
                if (self.last_city=="quit"):
                    break
                #delete whitespaces on the ends
                self.last_city=self.last_city.strip()
                #delete excesive spaces
                self.last_city=re.sub(" +"," ",self.last_city)
                #capitalize first letter of every word
                self.last_city=self.last_city.title()

                final_url=(self.wiki_url+self.last_city).replace(" ","_")
                try:
                    content=self.desoupify(final_url)
                except:
                    #This is for situtions like New York
                    try:
                        # self.last_city+="_self.last_city"
                        self.last_city+=" City"
                        final_url=(self.wiki_url+self.last_city).replace(" ","_")
                        content=self.desoupify(final_url)
                    except:
                        raise Exception("no results found")
                    else:
                        print("Did you mean {} \"City\"?".format(self.last_city[:-5]))
            except Exception as x:
                print(x)
                print("Sorry, can't find anything, please try again\n")
                continue
            
            #there are more words with mayor (like mayoral) but Al can be a name
            #mayoral can be found in London
            mayor_pattern=r"[^A-Za-z][Mm]ayor[^(alty)]" 
            dot=r"•"
            hyperlink_pattern=r"\[[0-9]*\]"
            content_table=[]
            prez=[]

            check_mayor=re.search(mayor_pattern,content)

            check_area=re.search(r"Area",content)
            if(check_mayor) and (check_area):
                content=content[check_mayor.end()-1:check_area.start()] #-1 because of regex looking for any character
                check_dot=re.search(dot,content)
                #all this code below to check if there is more than one mayor (aka Jerusalem Exception,
                # check Jerusalems mayor on wikipedia and see for yourself)
                while (check_dot)and(check_mayor):
                    content_table.append(content[:check_dot.start()].strip())
                    content=content[check_dot.end():]
                    check_mayor=re.search(mayor_pattern,content)
                    if (check_mayor):
                        content=content[check_mayor.end():]
                    check_dot=re.search(dot,content)
                
                if(check_mayor):
                    content_table.append(content.strip())

                for ind,con in enumerate(content_table): #need to manipulate the list so require index
                    check_hyper=re.match(hyperlink_pattern,con)
                    if(check_hyper):
                        con=con[check_hyper.end():]
                    check_hyper=re.search(hyperlink_pattern,con)
                    if (check_hyper):
                        con=con[:check_hyper.start()]
                    content_table[ind]=con
                
                # self.last_city=re.sub("_"," ",self.last_city)
                print("According to \""+final_url+"\":")
                for c in content_table:
                    print("The mayor of "+self.last_city+" is "+c)
                break
            else:
                print("Sorry, can't find anything, please try again\n")

    @classmethod
    def st_do_magic(cls):
        
        while(True):
            try:
                city=str(input("Tell me the city: "))
                if (city=="quit"):
                    break
                #delete whitespaces on the ends
                city=city.strip()
                #delete excesive spaces
                city=re.sub(" +"," ",city)
                #capitalize first letter of every word
                city=city.title()

                final_url=(cls.wiki_url+city).replace(" ","_")
                try:
                    content=cls.desoupify(final_url)
                except:
                    #This is for situtions like New York
                    try:
                        # city+="_city"
                        city+=" City"
                        final_url=(cls.wiki_url+city).replace(" ","_")
                        content=cls.desoupify(final_url)
                    except:
                        raise Exception("no results found")
                    else:
                        print("Did you mean {} \"City\"?".format(city[:-5]))
            except Exception as x:
                print(x)
                print("Sorry, can't find anything, please try again\n")
                continue
            
            #there are more words with mayor (like mayoral) but Al can be a name
            #mayoral can be found in London
            mayor_pattern=r"[^A-Za-z][Mm]ayor[^(alty)]" 
            dot=r"•"
            hyperlink_pattern=r"\[[0-9]*\]"
            content_table=[]
            prez=[]

            check_mayor=re.search(mayor_pattern,content)

            check_area=re.search(r"Area",content)
            if(check_mayor) and (check_area):
                content=content[check_mayor.end()-1:check_area.start()] #-1 because of regex looking for any character
                check_dot=re.search(dot,content)
                #all this code below to check if there is more than one mayor (aka Jerusalem Exception,
                # check Jerusalems mayor on wikipedia and see for yourself)
                while (check_dot)and(check_mayor):
                    content_table.append(content[:check_dot.start()].strip())
                    content=content[check_dot.end():]
                    check_mayor=re.search(mayor_pattern,content)
                    if (check_mayor):
                        content=content[check_mayor.end():]
                    check_dot=re.search(dot,content)
                
                if(check_mayor):
                    content_table.append(content.strip())

                for ind,con in enumerate(content_table): #need to manipulate the list so require index
                    check_hyper=re.match(hyperlink_pattern,con)
                    if(check_hyper):
                        con=con[check_hyper.end():]
                    check_hyper=re.search(hyperlink_pattern,con)
                    if (check_hyper):
                        con=con[:check_hyper.start()]
                    content_table[ind]=con
                
                # city=re.sub("_"," ",city)
                print("According to \""+final_url+"\":")
                for c in content_table:
                    print("The mayor of "+city+" is "+c)
                break
            else:
                print("Sorry, can't find anything, please try again\n")


    @classmethod
    def gui_do_magic(cls,city):
        try:
            #delete whitespaces on the ends
            city=city.strip()
            #delete excesive spaces
            city=re.sub(" +"," ",city)
            #capitalize first letter of every word
            city=city.title()

            final_url=(cls.wiki_url+city).replace(" ","_")
            try:
                content=cls.desoupify(final_url)
            except:
                #This is for situtions like New York
                try:
                    city+=" City"
                    final_url=(cls.wiki_url+city).replace(" ","_")
                    content=cls.desoupify(final_url)
                except:
                    raise Exception("no results found")
        except Exception as x:
            return "No results"
        
        #there are more words with mayor (like mayoral) but Al can be a name
        #mayoral can be found in London
        mayor_pattern=r"[^A-Za-z][Mm]ayor[^(alty)]" 
        dot=r"•"
        hyperlink_pattern=r"\[[0-9]*\]"
        content_table=[]

        check_mayor=re.search(mayor_pattern,content)

        check_area=re.search(r"Area",content)
        if(check_mayor) and (check_area):
            content=content[check_mayor.end()-1:check_area.start()] #-1 because of regex looking for any character
            check_dot=re.search(dot,content)
            #all this code below to check if there is more than one mayor (aka Jerusalem Exception,
            # check Jerusalems mayor on wikipedia and see for yourself)
            while (check_dot)and(check_mayor):
                content_table.append(content[:check_dot.start()].strip())
                content=content[check_dot.end():]
                check_mayor=re.search(mayor_pattern,content)
                if (check_mayor):
                    content=content[check_mayor.end():]
                check_dot=re.search(dot,content)
            
            if(check_mayor):
                content_table.append(content.strip())

            for ind,con in enumerate(content_table): #need to manipulate the list so require index
                check_hyper=re.match(hyperlink_pattern,con)
                if(check_hyper):
                    con=con[check_hyper.end():]
                check_hyper=re.search(hyperlink_pattern,con)
                if (check_hyper):
                    con=con[:check_hyper.start()]
                content_table[ind]=con
            
            # city=re.sub("_"," ",city)
            # print("According to \""+final_url+"\":")
            # for c in content_table:
            #     print("The mayor of "+city+" is "+c)
            # break
            # return content_table[0]
            answer=""
            for c in content_table:
                answer+=c+"\n"
            answer=answer.strip()
            return answer

        else:
            print("Sorry, can't find anything, please try again\n")


    @staticmethod
    def desoupify(url):
        # page=urlopen(url)
        # soup=BeautifulSoup(page,"html.parser")
        # whole_table=soup.find("table",attrs={"class":"infobox"})
        # content=whole_table.text.strip()
        # return content
        return (BeautifulSoup(urlopen(url),"html.parser").find("table",attrs={"class":"infobox"})).text.strip()



# FindTheMayor.st_do_magic()

# thing=FindTheMayor()
# # print(thing.last_city)
# thing.do_magic()
# # print(thing.last_city)
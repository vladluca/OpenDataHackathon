from tkinter.constants import INSERT, END
import urllib.request

from bs4 import BeautifulSoup

from CrawlerProgram.Functions import get_page_list


url = 'http://data.gov.ro/'

def doCrawl(tx1, root): # Scrie in 'outputFile' linkurile de download pentru toate seturile de date (csv,xls,xml,etc)
    outputFile=open("D:\LINKDB.txt",'w')
    urls=get_page_list() # stack of urls to scrape
    visited = [url] #record of visited urls
    while len(urls) >0:
        tx1.delete("1.0", END)
        try:
            htmltext=urllib.request.urlopen(urls[0]).read()
        except:
            tx1.insert(INSERT, urls[0])
            root.update_idletasks()
        soup = BeautifulSoup(htmltext)
        
        urls.pop(0)
        tx1.insert(INSERT, len(urls))
        tx1.insert(INSERT, ": ")
        
        for tag in soup.findAll('a',href=True):
            tag['href'] = urllib.parse.urljoin(url,tag['href'])
    
            if url in tag['href'] and tag['href'] not in visited:
                if 'storage' in tag['href']:
                    tx1.insert(INSERT, tag['href'])
                    print(tag['href'])
                    outputFile.write(tag['href']+"\n")
                    root.update_idletasks()
                visited.append(tag['href'])
    outputFile.close()
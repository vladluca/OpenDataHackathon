import os.path
import sys
from tkinter.constants import INSERT, END
import urllib.request

from CrawlerProgram.Functions import file_len


filename = 'D:\LINKDB.txt'
total = file_len(filename)
current = 0
oldPerc = -1
wr = 0
rt = 0

def dlProgress(count, blockSize, totalSize): # Download progress of current file
    percent = int(count * blockSize * 100 / totalSize)
    oldPerc = -1
    if percent != oldPerc:
        wr.delete("1.0", END)
        wr.insert(INSERT, str(current) + ' / ' + str(total) + ' ... ' + str(percent) + '% of current file (' + 
               str(round((count * blockSize) / 1000000, 2)) + '/' +
               str(round(totalSize / 1000000, 2)) + ' Mb )'
              )
        print(str(current) + ' / ' + str(total) + ' ... ' + str(percent) + '% of current file (' + 
               str(round((count * blockSize) / 1000000, 2)) + '/' +
               str(round(totalSize / 1000000, 2)) + ' Mb )')
        rt.update_idletasks()
        oldPerc = percent
    sys.stdout.flush()


def UpdateDatabase(tx1, root): # Parcurge 'filename' rand cu rand si descarca fisierele in 'download_folder' (care nu exista)
    download_folder="D:\\descarcari\\"
    filename = 'D:\LINKDB.txt'
    filess = open('D:\databaseFiles.txt','a')
    links = open(filename, 'r')
    notwritten=[]
    global wr
    global rt
    global current
    
    wr = tx1
    rt = root
    
    for link in links:
        link = link.strip()
        name = link.rsplit('/', 1)[-1]
        filename = str(download_folder) + str(name)
    
        if not os.path.isfile(filename):
            wr.delete("1.0", END)
            print('Downloading: ' + link)
            print( 'In: ' + filename)
            #rt.update_idletasks()
            try:
                urllib.request.urlretrieve(link, filename, reporthook=dlProgress)
                current += 1
                filess.write(filename+"\n")
            except Exception as inst:
                tx1.insert(INSERT, inst)
                tx1.insert(INSERT, '  Encountered unknown error. Continuing.')
        else:
            notwritten.append(filename)
    wr.insert(INSERT, "Done!") # Afiseaza fisierele care nu s-au descarcat

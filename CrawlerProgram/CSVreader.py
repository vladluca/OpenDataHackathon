import csv
import time
from tkinter.constants import INSERT, END

from CrawlerProgram.Functions import get_csv_header_list, get_csv_delimiter


filename = 'D:\databaseFiles.txt'
exact=-1
throw = 0

def doRowSplit(row,delimiter,columns):
    i=0
    while i<len(row)-1:
        if row[i-1]==row[i]=='"':
            row=row[:i-2]+row[i:]
        i+=1
    
    if (delimiter == ',' and '"' in str(row)):
        rowList=row
        i=0
        while i<len(rowList):
            if rowList[i] != '"':
                i+=1
            else:
                j=i+1
                while j<len(rowList)-1 and rowList[j]!='"':
                    j+=1
                for x in range(i,j):
                    if rowList[x]==',':
                        newRowList=rowList[:x]+';'+rowList[x+1:]
                        rowList=newRowList
                i=j+1
        rowList=rowList.split(delimiter)
        return rowList
    else:
        return row.split(delimiter)

def doSearchInCSV(terms,text,tx1, master): # Cauta termenul 'term' in toate fisierele CSV din 'filename' si le scrie in 'ResultPath'
    print("Working...")
    
    global throw
    throw = 0
    start_time=time.time()
    totalResults=0
    eTerms=terms
    terms=terms.split(' ')
    lght=len(terms)
    Olen=lght
    for i in range(0,lght):
        terms.append(terms[i].upper())
        terms.append(terms[i].lower().capitalize())
            
    lght=len(terms)

    for line in open(filename,'r').readlines():      
        line=line[:-1]
        if line.endswith('.csv'):
                currentResults=0
                columns=get_csv_header_list(line)
                delimiter=get_csv_delimiter(line)
                tx1.delete("1.0", END)
                tx1.insert(INSERT, line+'\n')
                master.update_idletasks()
    
                columns[len(columns)-1]=columns[len(columns)-1].replace('\n','')
                
                OpenedFile=open(line,'r',encoding='ISO 8859-1')
                OpenedFile=OpenedFile.readlines()
                if exact == 1:
                    for row in OpenedFile:
                        if(throw == 1):
                                raise Exception 
                        if len(terms)==1:
                            eTerms=' '+eTerms+' '
                        if eTerms.lower() in row or eTerms.upper() in row or eTerms.lower().capitalize() in row:
                            CurrentRow=doRowSplit(row,delimiter,columns)
                            currentResults+=1
                            for i in range(0,len(CurrentRow)):
                                try:
                                    resultString=str('\n'+columns[i])+':'+str(CurrentRow[i])
                                    text.insert(INSERT,resultString.encode('ISO 8859-1'))
                                    master.update_idletasks()
                                except:
                                    print(CurrentRow)
                                    print(i)
                else:   
                    for precision in range(Olen,0,-1):
                        for row in OpenedFile:
                            if(throw == 1):
                                raise Exception  
                            if str(terms) in row:
                                CurrentRow=doRowSplit(row,delimiter,columns)
                                currentResults+=1
                                for i in range(0,len(CurrentRow)):
                                    try:
                                        resultString=str('\n'+columns[i])+':'+str(CurrentRow[i])
                                        text.insert(INSERT,resultString.encode('ISO 8859-1'))
                                        master.update_idletasks()
                                    except:
                                        break   
                            else:
                                found=0
                                for si in range(0,lght):
                                    if terms[si] in row:
                                        found+=1
                                if found==precision and found > 0:#'row' contains search term
                                    currentResults+=1
                                    if currentResults==1:
                                        text.insert(INSERT,'\n#########################################################################################\n')
                                        text.insert(INSERT,'Results in: '+line+'\n')
                                    CurrentRow=doRowSplit(row,delimiter,columns)
                                    for i in range(0,len(CurrentRow)):
                                                if CurrentRow[i]!='' and CurrentRow[i]!='\n':
                                                    if len(CurrentRow[i]) > 100:
                                                        CurrentRow[i]=CurrentRow[i][:100]+' ...'
                                                    try:
                                                        if CurrentRow[i]!=columns[i]:
                                                            resultString=str('\n'+columns[i])+':'+str(CurrentRow[i])
                                                            text.insert(INSERT,resultString.encode('ISO 8859-1'))
                                                            master.update_idletasks()
                                                    except:
                                                        pass
                                    break
                totalResults+=currentResults
                if currentResults > 0:
                    resultString='\n'+str(currentResults)+" results in" +str(line)
                    tx1.insert(INSERT,resultString+'\n')
                    master.update_idletasks()
    print('DONE')
    tx1.insert(INSERT, 'DONE')
    tx1.insert(INSERT,'\nTotal results : '+str(totalResults))
    master.update_idletasks()   
    tx1.insert(INSERT,"\nDone in %.2f" % (time.time()-start_time)+" seconds.")
    
    
def doas():
    global throw
    throw = 1


def set_exact():
    global exact
    exact = exact * -1
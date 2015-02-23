import urllib.request
import unicodedata
import codecs
import chardet
rootURL = 'http://data.gov.ro/dataset/'
def get_page_list(): # Returneaza o lista de pagini care contin seturi de date
    dataSetList = 'http://data.gov.ro/api/3/action/package_list'
    htmltext = urllib.request.urlopen(dataSetList).read()
    result = str(htmltext, encoding='utf-8')
    result = result.replace('"', '').replace(' ', '')
    result = result.replace('{', '').replace('}', '')
    result = result.replace('[', '').replace(']', '')
    result = result.split(',')
    result.pop(0)
    result.pop(0)
    result.pop(0)
    for i in range(0, len(result)):
        result[i] = str(rootURL) + str(result[i])
    return result

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_csv_delimiter(path):
    max=0
    candidates={}

    test=open(path,'rb').readline()
    
    Ncoding=chardet.detect(test)
    Ncoding=Ncoding['encoding']
    if Ncoding == 'ascii':
        Ncoding = 'utf-8'
    header=open(path,'r',encoding=Ncoding).readline()
    
    #print()
    #print(str(header.encode(Ncoding)))
    for i in range(0,len(header)):
        candidates[header[i]]=0
    for i in range(0,len(header)):
        if not header[i].isalnum():
            candidates[header[i]]+=1
    for i in candidates:
        if candidates[i]>max and not i.isalnum() and i != ' ':
            max=candidates[i]
            delimiter=i
    #print(str(max)+' '+str(delimiter)+str(path))
    return delimiter

def get_csv_header_list(path):
    delimiter=get_csv_delimiter(path)
    header=open(path,'r',encoding='ISO 8859-1').readline()
    return header.split(delimiter)
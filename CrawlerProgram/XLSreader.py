'''
Created on Feb 21, 2015

@author: Vlad
'''

import traceback
import sys

import time
from tkinter.constants import END, INSERT

from xlrd import *


filename = 'D:\databaseFiles.txt'




def format_exception(e):
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1]))

    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception_list)
    # Removing the last \n
    exception_str = exception_str[:-1]

    return exception_str




def Read_from_xls(term, tx1, text,  master):
    #open and read XLS
    
    print (term)
    print("Working...")
    start_time=time.time()
    totalResults=0
    currentResults=0
    loweredInput=term.lower()
    upperedInput=term.upper()
    
    
    for line in open(filename,'r').readlines():
        try:
            line=line[:-1]
            if line.endswith('.xls'):
                currentResults=0
                #columns=get_csv_header_list(line)
                #delimiter=get_csv_delimiter(line)
                tx1.delete("1.0", END)
                tx1.insert(INSERT, line+'\n')
                master.update_idletasks()
        
        
                book = open_workbook(line, on_demand = True, encoding_override='ISO 8859-1') 
                i = 1
                while i <= book.nsheets:
                    try:
                        act_sheet = book.sheet_by_index(i - 1)
                        curr_row = -1
                        while curr_row < act_sheet.nrows - 1:
                            curr_row += 1
                            row = act_sheet.row(curr_row)
                            curr_cell = 0
                            while curr_cell < act_sheet.ncols - 1:
                                cell_val = str(act_sheet.cell_value(curr_row, curr_cell))
                                if loweredInput in cell_val or upperedInput in cell_val:
                                    currentResults += 1
                                    #text.insert(INSERT, act_sheet.name)
                                    #text.insert(INSERT, curr_row + 1)
                                    #text.insert(INSERT, act_sheet.row_values(curr_row))
                                    #text.insert(INSERT, '\n')
                                curr_cell += 1        
                        i += 1
                    except:
                        i += 1
            totalResults+=currentResults
            if currentResults > 0:
                resultString='\n'+str(currentResults)+" results for "+str(term)+" in "+str(line)
                text.insert(INSERT,resultString+'\n')
                master.update_idletasks()
        except Exception as e:
            print(i)
            print(curr_cell)
            print(curr_row)
            print(line)
            print ("Printing only the traceback above the current stack frame")
            print ("".join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])))
            print()
            print ("Printing the full traceback as if we had not caught it here...")
            print (format_exception(e))
    tx1.insert(INSERT, 'DONE')
    text.insert(INSERT,'\nTotal results : '+str(totalResults))
    master.update_idletasks()   
    text.insert(INSERT,"\nDone in %.2f" % (time.time()-start_time)+" seconds.")
                
                
                
                
                
                
#Read_from_xls("admitere", "D:\Marius\Liclipse Workspace\date-statistice-ana-2014.xls")








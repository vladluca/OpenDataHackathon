'''
Created on Feb 20, 2015

@author: Vlad
'''



from _thread import start_new_thread
from tkinter import *

from CrawlerProgram.CSVreader import doSearchInCSV, exact, set_exact
from CrawlerProgram.CSVreader import doas
from CrawlerProgram.Main import doCrawl
from CrawlerProgram.XLSreader import Read_from_xls
from CrawlerProgram.XMLreader import makeSearchInXML
from CrawlerProgram.downloader import UpdateDatabase


try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
    


def stopProg():
    root.destroy()
    


def make_entry(parent, caption):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

    
def check_search():
    text.delete("1.0", END)
    z = 0
    desearch = user.get()
    if(len(desearch) != 0):
        for i in range(0, len(a)):
            if(desearch) in a[i]:
                text.insert(INSERT, a[i])
                text.insert(INSERT, '\n')
                z = z + 1
        if(z == 0):
            text.insert(INSERT, "No result for: ")
            text.insert(INSERT, desearch)


threads=[]

def hack_search(*arg):
    
    text.delete("1.0", END)
    tx1.delete("1.0", END)
    p = user.get()
    i = 0
    if(len(p) != 0):
        #start_new_thread(Read_from_xls, (user.get(), tx1, text, root))
        start_new_thread(doSearchInCSV, (user.get(), text, tx1, root))
        #start_new_thread(makeSearchInXML,("D:\\databaseFiles.txt", user.get(), text, tx1, root))
        #doSearchInCSV(user.get(), text, tx1, root)



def update_data(*arg):
    tx1.delete("1.0", END)
    text.delete("1.0", END)
    start_new_thread(doCrawl, (tx1,root))
    #doCrawl(tx1, root)


def update_files(*arg):
    text.delete("1.0", END)
    tx1.delete("1.0", END)
    start_new_thread(UpdateDatabase, (tx1,root))
    #UpdateDatabase(tx1, root)


def stopAS():
    doas()

def set_strict():
    set_exact()

root = tk.Tk()
#root.tk.call('encoding', 'system', 'ISO 8859-1')
root.resizable(0, 0)
root.geometry('1200x850')
root.title('Search Engine')




parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)

frame1 = Frame(parent, bd=0, relief=SUNKEN)

frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)

f = tk.Button(frame1, borderwidth=2, text="Update data", width=12, pady=4, command=update_data)
f.grid(row = 0, column = 0)

c = tk.Button(frame1, borderwidth=2, text="Update files", width=12, pady=4, command=update_files)
c.grid(row = 0, column = 2)

frame1.pack()

user = make_entry(parent, "Enter text:")

root.bind('<Return>', hack_search)



b = tk.Button(parent, borderwidth=2, text="Search", width=12, pady=4, command=hack_search)
b.pack()
user.focus_set()

global exact
var = exact

y = Checkbutton(parent, text="Exact string", command = set_strict)
y.pack()




#tx1 = Text(parent, width = 30, height = 10)
#tx1.pack()

#e = Label(parent, text = "Results:")
#e.pack()

frame1.pack()

frame = Frame(parent, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)


e = Label(frame, text = "Results:")
e.grid(row = 0, column = 0, sticky=N+S)

d = Label(frame, text="Executing:")
d.grid(row = 0, column = 3, sticky = N+S)

yscrollbar = Scrollbar(frame)
ysecond = Scrollbar(frame)
yscrollbar.grid(row=1, column=1, sticky=N+S)
ysecond.grid(row=1, column=4, sticky=N+S)

text = Text(frame, wrap=WORD, bd=0, width = 100, height = 39, yscrollcommand=yscrollbar.set)

text.grid(row=1, column=0, sticky=N+S+E+W)

tx1 = Text(frame, wrap = WORD, bd = 0, width = 40, height = 39, yscrollcommand = ysecond.set)
tx1.grid(row = 1, column = 3, sticky = N+S+E+W)

yscrollbar.config(command=text.yview)
ysecond.config(command=tx1.yview)

frame.pack()






#scrollbar = Scrollbar(parent)
#scrollbar.pack(side=RIGHT, fill=Y)

#text = Text(parent, width=60, height=20, yscrollcommand=scrollbar.set)
#text. insert(INSERT, "Press any button!")
#text. pack()

#scrollbar.config(command=text.yview)





a = tk.Button(parent, borderwidth=2, text="Stop Search", width=12, pady=4, command = stopAS)
a.pack()


#a = ["ana", "maria", "georgeta", "cal batran"]


parent.mainloop()
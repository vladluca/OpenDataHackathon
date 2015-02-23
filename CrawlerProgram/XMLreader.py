'''
Created on Feb 22, 2015

@author: Vlad
'''
'''
Created on Feb 22, 2015

@author: Vlad
'''

import sys
from tkinter.constants import END, INSERT
from xml.etree import ElementTree


def indent(elem, level=0):

    i = "\n" + level*"  "

    if len(elem):

        if not elem.text or not elem.text.strip():

            elem.text = i + "  "

        if not elem.tail or not elem.tail.strip():

            elem.tail = i

        for elem in elem:

            indent(elem, level+1)

        if not elem.tail or not elem.tail.strip():

            elem.tail = i

    else:

        if level and (not elem.tail or not elem.tail.strip()):

            elem.tail = i



def searchInXML(path, word, encoding):

    """

    """

    #f = open(path, "r")

    #line = f.readline()

    root = ElementTree.parse(path).getroot()

    indent(root)

    all = ElementTree.tostring(root, encoding, "html")

    lines = all.split("\n")

    lastSpace = 0

    allColumns = []

    ok = 0

    alls = []

    #for line in lines:

     #   print (line)

        

    for line in lines:

    #while line != "":

        spaces = 0

        for sp in line:

            if sp != " ":

                break

            spaces += 1

        allColumns.append(line)

        if line.find(word) != -1:

            ok = 1

            

        if spaces < lastSpace:

            if ok == 1:

                i = 0

                s = ""

                for col in allColumns:

                    if i != 0 and i != len(allColumns) - 1:

                        #print(col, end=" ")

                        for j in range(0, len(col)):

                            if col[j] == "<":

                                j += 1

                                try:

                                    while col[j] != ">":

                                        s += col[j]

                                        #print(col[j], end="")

                                        j += 1

                                    s += ": "

                                    #print(": ", end="")

                                    j += 1

                                    while col[j] != "<":

                                        s += col[j]

                                        #print(col[j], end="")

                                        j += 1

                                    s += "\n"

                                    #print("")

                                except:

                                    break

                                break

                            j += 1

                    i += 1

                #print(s)

                alls.append(s)

            ok = 0

            allColumns = []

        lastSpace = spaces

        #line = f.readline()

        

    return alls



def searchStringInXML(path, str, encoding, text, root):

    """

    """

    cuvs = str.split(" ")

    alls = searchInXML(path, cuvs[0], encoding)

    total = 0

    for s in alls:

        found = 0

        for cuv in cuvs:

            if s.find(cuv) != -1:

                found +=1

        #print(found, len(cuvs))

        if found == len(cuvs):

            total += 1

            #print(s)
    if(total > 0):
        text.insert(INSERT, '\n')
        text.insert(INSERT, total)
        text. insert(INSERT, " results in "+path)
        root.update_idletasks()
        

    

def makeSearchInXML(filename, term, text, tx1, root):

    for line in open(filename, 'r').readlines():

        if True:

            line = line[:-1]

            if line.endswith('.xml'):
                
                tx1.delete("1.0", END)
                tx1.insert(INSERT, line)
                tx1.insert(INSERT, '\n')
                root.update_idletasks()

                searchStringInXML(line, term, "unicode", text, root)
            tx1.insert(INSERT, "DONE!")

        
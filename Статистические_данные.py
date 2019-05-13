# Import `load_workbook` module from `openpyxl`
import os
from openpyxl import load_workbook
import io
import re


pattern = re.compile(r'\w+')
PathData = ('./Data/')
ListSheet = []
PathFiles = os.listdir(path=PathData)
PathToFile = "String"
StrRead = "a"
a="String"
ValueVariable=0
n=3
Dict = {}


#print(PathData)




class PathDocs(object):
    """docstring"""
 
    def __init__():
        """Constructor"""

    def ConfigChecker():
        with io.open('./Sys/Data.txt', encoding='utf-8') as file:
            for line in file:
                x = re.sub("^\s+|\n|\r|\s+$", '', line)

                Data = open('config.txt', 'r')
                lineS = Data.readline()
                while lineS:
                    #print(locals())
                    if((len(pattern.findall(lineS)))!=0):
                        if((len(pattern.findall(lineS)))==2):
                            #print(str(pattern.findall(lineS)[0]) +" = "+ str(pattern.findall(lineS)[1]))
                            #exec("%s = %d" % ((str(pattern.findall(lineS)[0])),float(str(pattern.findall(lineS)[1]))))
                            NameVar = str(pattern.findall(lineS)[0])
                            ValueVar = (float(str(pattern.findall(lineS)[1])))

                            Dict.update({NameVar: ValueVar})

                            #Dict[NameVar] = ValueVar
                            lineS = Data.readline()

                        if((len(pattern.findall(lineS)))==3):
                            #print(str(pattern.findall(lineS)[0]) +" = "+ str(pattern.findall(lineS)[1]) +"."+ str(pattern.findall(lineS)[2]))
                            NameVar = str(pattern.findall(lineS)[0])
                            ValueVar = (float(str(pattern.findall(lineS)[1])+"."+str(pattern.findall(lineS)[2])))
                            Dict.update({NameVar: ValueVar})
                            #Dict[NameVar] = ValueVar
                            #exec("%s = %d" % (NameVar,ValueVar))
                            #print(str(NameVar)+" = " + str(ValueVar))
                            lineS = Data.readline()

                    else:
                        #print(SugarMax)
                        break
                break


    
    def CheckListFiles():
        print("Начата проверка списка файлов в папке /Data/...")
        i=0
        for item in PathFiles:
            print(str(i+1)+"."+item)
            i=+1
        print("Проверка списка файлов в папке /Data/ успешно завершена...")
    def OpenFile():
        i=0
        FileName = PathFiles[int(input("Какой фаил открыть?\n"))-1]
        PathToFile = ((PathData)+str(FileName))
        print(PathToFile)
        return PathToFile
    def SheetList():
        wb = load_workbook(PathToFile)
        i=0
        print("Найденые таблицы в документе:")
        for sheet in wb:           # go over all sheets 
            print(str(i+1)+"."+str(sheet.title))
            ListSheet.append(sheet)
            i+=1
        sh = wb.active  

    def PrintData(row1,column1):
        print(ListSheet[0].cell(row=row1, column=column1).value)

   


PathDocs.ConfigChecker()
print(Dict.items())
PathDocs.CheckListFiles()
PathToFile = PathDocs.OpenFile()
PathDocs.SheetList()
print(PathDocs.PrintData(3,3))



'''
for i in range(1, 5):
     print(i, sh.cell(row=1, column=i).value)
'''





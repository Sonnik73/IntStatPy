# Import `load_workbook` module from `openpyxl`
import os
from openpyxl import load_workbook


PathData = ('./Data/')
ListSheet = []
PathFiles = os.listdir(path=PathData)
PathToFile = "String"
#NameSheet

print(PathData)




class PathDocs(object):
    """docstring"""
 
    def __init__():
        """Constructor"""
    def CheckListFiles():
        i=0
        for item in PathFiles:
            print(str(i+1)+"."+item)
            i=+1
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







PathDocs.CheckListFiles()
PathToFile = PathDocs.OpenFile()
PathDocs.SheetList()
print(PathDocs.PrintData(3,3))



'''
for i in range(1, 5):
     print(i, sh.cell(row=1, column=i).value)
'''





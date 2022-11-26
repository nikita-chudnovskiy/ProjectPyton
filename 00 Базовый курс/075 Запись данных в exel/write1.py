import openpyxl
import json
with open('111.json') as file:
    data =json.load(file)
print(data)



book = openpyxl.Workbook()
sheet = book.active

sheet['A1']='ID'
sheet['B1']='TITLE'
sheet['C1']='YEAR'
sheet['D1']='DIRECTOR'


book.save('111.xlsx')
book.close()



sheet = book.active
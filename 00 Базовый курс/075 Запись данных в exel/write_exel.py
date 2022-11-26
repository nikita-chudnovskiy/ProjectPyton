import openpyxl

book = openpyxl.Workbook()
sheet = book.active

sheet['A2']=100
sheet['B3']='Nikita'


sheet[1][0].value='world'
sheet.cell(row=1,column=3).value ='hello world'

book.save('my_book.xlsx')
book.close()
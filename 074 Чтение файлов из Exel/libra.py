import openpyxl

book = openpyxl.open("2.xlsx",read_only=True)
a = book.active
#print(a[2][0].value)

# for i in range(1,a.max_row+1):
#    author =a[i][0].value
#    name =a[i][1].value
#    year =a[i][2].value
#    rating =a[i][3].value
#    print(author,name,year,rating)

# ceels =a["B1":"D5"] # Диапазон рядом стоящие
# for name,year,rating in ceels:
#     print(name.value,year.value,rating.value)


for row in a.iter_rows(): # Если не передавать значение то выведет весь  (min_row=1,max_row=20,min_col=1,max_col=5)
    for cell in row:
        print(cell.value,end =' ')
    print()
# sheets_2 = book.worksheets[2] # 0,1,2 листы !!!!начинаются с 0
# print(sheets_2["A1"].value)
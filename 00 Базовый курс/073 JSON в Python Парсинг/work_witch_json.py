# JSON текстовый формат обмена данными похожи на словарь
import json

with open('file.txt', 'r') as nas_file:
    a=json.load(nas_file)

del a['name']

print(a)

a["mass"] =[1,'h',{'a':1},[1,2,3]]
print(json.dumps(a,indent =2))
#
with open('file.txt', 'w') as nas_file:
     json.dump(a,nas_file,indent=4)



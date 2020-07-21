#Sample Input 1:

#a
#Mary had a little lamb.

#Sample Output 1:
#Mary
#had
#a
#lamb.

#a
letter = input()
text = 'Mary had a little lamb.'
k=[]
for i in text.split():
    if letter in i.lower():
        print(i)


#e

letter = input()
text = 'Actions speak louder than words'
k=[]
for i in text.split():
    if letter in i.lower():
        print(i)
        k.append(i)
print(k)



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
text = input()
for i in text.split():
    if letter in i.lower():
        print(i)


#e

e = input()
text = input()
for i in text.split():
    if e in i.lower():
        print(i)



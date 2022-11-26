a = 'Abc1!@#AABB34defyubjz8#('
letters = [0] * 26
for i in a.lower(): # Все буквы маленькие
    if i >= 'a' and i <= 'z': # отсечем все сиволы
        nomer = ord(i) - 97 #перевод в цифры вычитаем
        letters[nomer]+=1
for i in range(26):
    print(chr(i+97),letters[i])
# Магия !
print()
s ='abdfbvz'
for i in s:
    print(i,ord(i)-97 )
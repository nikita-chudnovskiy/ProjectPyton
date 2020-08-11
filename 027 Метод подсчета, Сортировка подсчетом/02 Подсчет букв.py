a = 'Abc1!@#AABB34defyubjz8#('
letters = [0] * 26

for i in a.lower():
    if i >= 'a' and i <= 'z':
        nomer = ord(i) - 97
        letters[nomer]+=1
for i in range(26):
    print(chr(i+97),letters[i])
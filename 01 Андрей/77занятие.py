# import random
# f = open('words.txt',encoding='utf-8')
# text = f.read()
# words = text.split()
# word = random.choice(words)
# letters = []
# for i in range(len(word)):
#     letters.append('-')
# for i in range(len(word)+2):
#     print(*letters)
#     g = input('Введите букву: ')
#     if g not in word:
#         print('такой буквы нет')
#     else:
#         for idx in range(0,len(word)):
#             if word[idx] == g:
#                 letters[idx] = g
#     if '-' not in letters:
#         break

# h = []
# for i in range(2):
#     b = int(input())
#     h.append(b)
# print(max(h))


a = int(input())
k = int(input())
if a > k:
    print(1)
if a < k:
    print(2)
if a == k:
    print(0)

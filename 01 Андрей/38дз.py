f = open('pd.txt','r',encoding = 'utf-8')
text1 = f.read()
f.close()

# words = text1.split()
# b = 0
# for i in words:
#     if i[0] in 'аоеёюиэуыя' and i[-1] in 'аоеёюиэуыя':
#         b = b+1
# print(b)

# words = text1.split()
# for i in words:
#     if i[0] in 'йцкнгшщзхъфвпрлджчсмтьб' and i[-1] in 'йцкнгшщзхъфвпрлджчсмтьб':
#         print(i)

# words = text1.split()
# for i in words:
#     if i.count('а') == 3:
#         print(i)
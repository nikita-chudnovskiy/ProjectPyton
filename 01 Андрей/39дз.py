f = open('pd.txt','r',encoding = 'utf-8')
text1 = f.read()
f.close()

# words = text1.split()
# for i in words:
#     if len(i) > 1 and i[1] in 'йцкнгшщзхъфвпрлджчсмтьб':
#         print(i)

# words = text1.split()
# for i in words:
#     if i[0] in 'йцкнгшщзхъфвпрлджчсмтьб' and i[-1] in 'аеёоэиюяуы':
#         print(i)

# words = text1.split()
# for i in words:
#     if len(i) >3 and i[0:3] == 'про':
#         print(i)
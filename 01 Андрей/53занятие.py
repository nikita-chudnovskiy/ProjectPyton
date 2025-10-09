# def task1(lst1,lst2):
#     lst3 = []
#     for i in lst1:
#         if i in lst2:
#             lst3.append(i)
#     return(lst3)
#
# d = task1([4,7,1,8],[5,1,9,4])
# print(d)

# import random
# def wasd():
#     f = []
#     for i in range(10):
#         d = random.randint(1,100)
#         f.append(d)
#     return(f)
#
# s = wasd()
# print(s)

import requests
url = 'http://numbersapi.com/2025'
s = requests.get(url)
if s.status_code == 200:
    print(s.text)
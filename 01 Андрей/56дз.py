# import requests
# a = input()
# param = {
#     'name':a
# }
# t = requests.get('https://api.agify.io/',param)
# if t.status_code == 200:
#     g = t.json()
#     print(g['age'])


# import requests
# a = input()
# e = requests.get('https://api.genderize.io/?name='+a)
# if e.status_code == 200:
#     g = e.json()
#     print(g['gender'])


# import requests
# f = 0
# m = 0
# for i in range(5):
#     d = input()
#     y = requests.get('https://api.genderize.io/?name='+d)
#     e = y.json()
#     if e['gender'] == 'male':
#         m = m+1
#     if e['gender'] == 'female':
#         f = f+1
# print('Мужчин:',m)
# print('Женщин:',f)
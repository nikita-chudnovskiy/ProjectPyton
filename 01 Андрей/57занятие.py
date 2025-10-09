# import requests
# q = requests.get('https://official-joke-api.appspot.com/random_joke')
# if q.status_code == 200:
#     t = q.json()
#     print(t['setup'])
#     print(t['punchline'])


# def inter(r,h):
#     q = []
#     for i in r:
#         if i in h:
#             q.append(i)
#     return(q)
# rh = inter([2,7,5,9],[2,4,8,5])
# print(rh)

# def inter3(t,y,o):
#     g = []
#     for s in t:
#         if s in y and s in o:
#             g.append(s)
#     return(g)
# qwerty = inter3([9,12,6,3,4],[6,7,2,12,3],[3,9,8,12,2])
# print(qwerty)
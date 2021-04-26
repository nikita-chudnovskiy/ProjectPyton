worlds ={}
while True:
    s =input()
    if s in worlds:
        print('Слово',s,'переводится как',worlds[s])
    else:
        print('вв перевод слова',s)
        worlds[s]=input()

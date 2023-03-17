
text=input("Введите строку ")
search =input("Подстрока которую найти ")

def find_index(text, search):


    l1 = []
    index=0
    for i in range(len(text)):
        i = text.lower().find(search, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1


print(find_index(text, search))
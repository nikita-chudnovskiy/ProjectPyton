kol_mesyacev=12
cumma = 100000
procent = 10
platej=0
osn_plat=100000/12
pereplata=0
procent_bank=osn_plat/100*30
sp1 = ['янвварь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
for j in range(len(sp1)):
    platej = cumma / 100 * procent / 12
    print(j+1,sp1[j], platej)
    pereplata += platej


print('Основной платеж',osn_plat+platej)
print('Переплата',pereplata)



# Налог после уплаты 13 %, сумма 20000 не облагается

zp = int(input('Введите зп до вы  чета 13 % '))
if zp <= 20000:
    print(zp,'Зарплата После вычета 13 % ')
elif zp >20000:
    nalog = zp/100*13
    zp = zp-nalog
    print(zp,'Зарплата После вычета 13 % ')
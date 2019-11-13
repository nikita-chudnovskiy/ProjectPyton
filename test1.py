amount = float(input("Сколько хотите взять денег: "))
pct = int(input("Под какой процент вам их дают: "))

years = float(input("Насколько лет берете: "))

pct = pct / 100
month_pay = (amount * pct * (1 + pct) ** years) / (12 * ((1 + pct) ** years - 1))
print("Ваш месячный платеж составит: %.2f" % month_pay)

summa = month_pay * years * 12
print("За весь период вы заплатите: %.2f" % summa)
print("Это составит %.2f%% от первоначальной суммы" % ((summa / amount) * 100))



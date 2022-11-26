# Изменить строку @
d = 'Bilbo.Baggins@bagend.hobbiton.shire.me'
print(d.find('@'))
d = d.replace('@', '')  # Убираем  @ медотом replace и сразу переворачиваем
print(d)
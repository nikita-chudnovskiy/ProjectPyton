"""
\n  Перевод строки
\\ Символ обратного слеша
\’  Символ апострофа (одинарной кавычки)
\"  Символ двойной кавычки
\b  Эмуляция клавиши BackSpace
\r  Возврат каретки
\t  Горизонтальная табуляция
"""

print("Тема занятия \"спецсимволы\"")


#  На выходе Hello\Balakirev!
s="Hello Balakirev!".split()
print("\\".join(s))

# My best friend is Python!

# My'best"friend"is"Python!

s="My best friend is Python!".split()
s="\"".join(s)
s=s.replace("\"","\'",1)
print(s)


# r от слова raw, т.е r – это сырые строки (необработанные строки).
print(r"C:\WINDOWS\System32\drivers\etc\hosts")


# Подставить слово в кавычки
s="Война и Мир !"
print("\""+s+"\"")
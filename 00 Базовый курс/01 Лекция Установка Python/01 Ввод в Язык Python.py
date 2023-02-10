# У Pythona очень простой синтаксис . на нем очень легко как писать программы так и читать.

# Python является кросплатформенным , программа запущенная на windows легко запустится на любой другой ОС Mac ? linux
# Python очень многофункциональный, у него очень много библиотек, можно написать Desctop приложения , web, игры ,
# скрипты , ботов под сайты, Нанем проходят олимпиадное программирнование ЕГЭ. актуальная версия 3
# https://www.python.org/downloads/release/python-381/   запускаем жмем add python patch  ручная установка изменим путь установки
# Python37


"""
1.  Используйте длинные описательные имена, которые легко читаются.
    Очень важно, чтобы имена были простыми и описательными и могли быть поняты сами по себе.
    Это избавит от необходимости писать комментарии:
"""


# Not recommended
# The au variable is the number of active users
au = 105

# Recommended
total_active_users = 105



"""
2. Используйте информативные названия. Ваши коллеги и разработчики должны быть в состоянии выяснить, 
    какой у вас тип переменной и что она хранит по имени. 
    Короче говоря, ваш код должен быть легко читаемым и осмысленным.
"""

# Not recommended
c = ["UK", "USA", "UAE"]

for x in c:
    print(x)


# Recommended
cities_list = ["UK", "USA", "UAE"]
for city in cities_list:
    print(city)


"""
3. Всегда используйте один и тот же словарь. Соблюдайте соглашение об именах. 
Соблюдение принятого соглашения об именах важно для устранения путаницы, 
когда другие разработчики работают над вашим кодом. 
И это относится к именованию переменных, файлов, функций и даже структур каталогов.
"""

# Not recommended
client_first_name = 'John'
customer_last_name = 'Doe'

# Recommended
client_first_name = 'John'
client_last_name = 'Doe'

# Another example:

# Not recommended
def fetch_clients(response, variable):
    # do something
    pass

def fetch_posts(res, var):
    # do something
    pass

# Recommended
def fetch_clients(response, variable):
    # do something
    pass

def fetch_posts(response, variable):
    # do something
    pass
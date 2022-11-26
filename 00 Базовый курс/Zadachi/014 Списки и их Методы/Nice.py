nice = list(map(int,input('введите оценки ').split()))
sum(nice)
sredniy_nice = sum(nice)/len(nice)
print(sredniy_nice)

if  sredniy_nice >=90:
    print('Very Good')
else:
    print('Bad')
a =input()
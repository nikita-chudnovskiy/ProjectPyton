from idlelib.rpc import request_queue

for i in range(1, 200): # Делится на 17
    if i % 17 == 0:
        print(i)
print()
print()
for i in range(1,200): # Числа оканчивающиеся на 4
    if i %10==4:
        print(i)
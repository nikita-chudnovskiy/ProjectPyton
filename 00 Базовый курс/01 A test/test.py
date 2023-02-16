import math

# i =0
# while i <10:
#     i += 1
#     if i ==5:
#         continue
#     print(i)



str = "JavaTpoint"
i=0
while i <len(str):
    if str[i]=="T":
        i += 1
        continue

    print(str[i])
    i += 1

import os
# for f in os.listdir('.'):
#     if f[-4:] == '.txt':
#         os.rename(f,'apple/'+f)

for k in os.listdir('apple'):
    os.rename('apple/'+k,'./'+k)
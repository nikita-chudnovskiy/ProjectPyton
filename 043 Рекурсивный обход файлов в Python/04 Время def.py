import timeit

def hello():
    print('hello')


hello()
print(timeit.timeit( stmt =hello,number =0))
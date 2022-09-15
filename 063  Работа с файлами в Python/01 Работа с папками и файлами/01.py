import os

def main_func():
    if not os.path.isdir(r'C:\papka'):
        os.mkdir(r'C:\papka')
main_func()

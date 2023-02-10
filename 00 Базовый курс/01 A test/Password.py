data =input()


def password(data):
    return not(len(data) < 10 or
            data.isdigit() or
            data.isalpha() or
            data.islower() or
            data.isupper())\
            and data.isalnum()

print(password(data))




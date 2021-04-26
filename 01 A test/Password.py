password = input()


def check(password):
    kool_s = 0

    for s in password:
        if s.isdigit():
            kool_s += 1
    print(kool_s)


check(password)

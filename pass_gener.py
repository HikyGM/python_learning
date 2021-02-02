import random


def generator_password(length: int):
    password = ''
    symb = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQASTUVWXYZ'
    for i in range(length):
        password += random.choice(symb)
    print(password)


def main():
    a = int(input())
    b = int(input())
    for i in range(a):
        generator_password(b)


main()
print(test)
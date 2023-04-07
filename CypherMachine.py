"""
A Cypher Machine to encrypt your files such that to
decrypt it you must know the date when the file was encrypted and
two keys.

Date Modified:  April 7, 2023
Author: Varnit Singh
"""


import random
import os

l1, l2 = [], []


def create_list(l):
    for i in range(97, 123):
        l.append(chr(i))
    for j in range(48, 58):
        l.append(chr(j))
    for k in range(65, 91):
        l.append(chr(k))
    symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '|',
               ';', '"', '\'', '<', ',', '>', '.', '?', '/', ' ', ':', '\\']
    l.extend(symbols)
    random.shuffle(l)


create_list(l1)
create_list(l2)


def rotate_clock(l):
    l.append(' ')
    for i in range(1, len(l)):
        l[-i], l[-i - 1] = l[-i - 1], l[-i]
    l[0], l[-1] = l[-1], l[0]
    l.pop(-1)


def rotate_anti(l):
    l.insert(0, ' ')
    for i in range(len(l) - 1):
        l[i + 1], l[i] = l[i], l[i + 1]
    l[0], l[-1] = l[-1], l[0]
    l.pop(0)


def clear(list1, list2):
    for i in range(len(list1)):
        list1[i] = list1[i][:-1]
        list2[i] = list2[i][:-1]


def create_key(l, key_name):
    with open('{a}.txt'.format(a=key_name), 'w') as file:
        for item in l:
            file.write(f'{item}\n')


def encrypt(string, date, month):
    global s2
    s2 = ''
    s = string
    for i in range(len(s)):
        a = l1.index(s[i])
        s2 = s2 + l2[a]
        for p in range(date):
            rotate_clock(l1)
        for q in range(month):
            rotate_anti(l2)

    with open('Encrypted_string.txt', 'w') as encrypt_string:
        for k in s2:
            encrypt_string.write(f'{k}')

    return s2


def decrypt(string, date, month):
    global out
    out = ''
    la, lb = [], []
    with open('Key1.txt', 'r') as file:
        for i in range(len(l2)):
            line = file.readline()
            la.append(line)
    with open('Key2.txt', 'r') as file1:
        for i in range(len(l1)):
            line1 = file1.readline()
            lb.append(line1)
    clear(la, lb)

    for k in range(len(string)):
        p = lb.index(string[k])
        out = out + la[p]
        for p in range(date):
            rotate_clock(la)
        for q in range(month):
            rotate_anti(lb)

    with open('Decrypted_string.txt', 'w') as decrypt_string:
        for k in out:
            decrypt_string.write(f'{k}')

    return out


print("1. Encrypt")
print("2. Decrypt")
print("3. Exit")
while True:
    inp = eval(input("Whats your choice (1/2/3) : "))

    if inp == 1:
        if os.path.exists('Encrypted_string.txt'):
            os.remove('Encrypted_string.txt')
        if os.path.exists('Key1.txt'):
            os.remove("Key1.txt")
        if os.path.exists('Key2.txt'):
            os.remove("Key2.txt")

        key_in = int(input("\nDo you want to create a new key ? \n1. Yes \n2. No \n"))
        if key_in == 1:
            create_key(l1, 'Key1')
            create_key(l2, 'Key2')

        print("\nCollect your keys from the same folder as CypherMachine")
        a, b = input("Enter date and month (dd_mm) : ").split()
        in_string = input("Enter the string : ")
        encrypted_string = encrypt(in_string, int(a), int(b))
        print("Encrypted string is : ", encrypted_string, "\n")
    elif inp == 2:
        if os.path.exists('Decrypted_string.txt'):
            os.remove('Decrypted_string.txt')
        print("Things to take care of : ")
        print("1. Both the keys that you need must be in the name of Key1.txt and Key2.txt.")
        print("1. Enter 'Key1.txt' and 'Key2.txt' in the same folder as CypherMachine")
        a, b = input("Enter date and month (dd_mm) : ").split()
        in_string = input("Enter encrypted string : ")
        print("Decrypted string is : ", decrypt(in_string, int(a), int(b)), "\n")
        print("Collect the decrypted string from the folder as same as the CypherMachine")
    elif inp == 3:
        break
    else:
        print("\nIncorrect input !! Try again.")
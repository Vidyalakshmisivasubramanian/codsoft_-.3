from random import*
import string

def passwd(a):
    password=''
    if upp=="yes":
        password+=string.ascii_uppercase
    if dig=="yes":
        password+=string.digits
    if pun=="yes":
        password+=string.punctuation
    if low=="yes":
        password+=string.ascii_lowercase
    print('Your Password is:  ',end='')
    for x in range(a):
        print(choice(password),end='')


a=int(input("\t\tPASSWORD GENERATOR\n\nEnter The Length of Your Password: "))
upp=input("Do You Prefer Upper Case Letters?(yes/no):").lower()
low=input("Do You Prefer Lower Case Letters?(yes/no): ").lower()
dig=input("Do You Prefer Numbers?(yes/no): ").lower()
pun=input("Do You Prefer Special Symbols?(yes/no):").lower()
passwd(a)

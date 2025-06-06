# A simple program to check whether a given number is palindrome,armstrong
import math
def palindrome():
    n=int(input("Enter any integer number: "))
    s=0
    a=n
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    print("Yes, Palindrome.....") if(a==s) else print("No, not a Palindrome.....")
    print("\n\n")

def armstrong():
    n=int(input("Enter any integer number: "))
    s=0
    a=n
    while(n>0):
        r=n%10
        s+=pow(r,3)
        n=n//10
    print("Yes, Armstrong.....") if(a==s) else print("No, not a Armstrong.....")
    print("\n\n")
print("Enter\n1. For Palindrome\n2. For Armstrong\n3. For Exit\n")
while(1):
    x=int(input("Enter (1-3): "))
    match(x):
        case 1:
            palindrome()
        case 2:
            armstrong()
        case 3:
            exit(1)
        case _:
            print("Invalid Input....Please Enter valid Input")



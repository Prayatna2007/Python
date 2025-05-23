def dec_to_bin():
    n=int(input("Enter a decimal integer:"))
    a=n
    i=0
    s=0
    while n>0:
        r = n%2
        s += r*pow(10,i)
        n=n//2
        i=i+1
    print(f"The Decimal value is {a} and Binary value is {s}")

def bin_to_dec():
    n=int(input("Enter any binary number:"))
    a=n
    i=0
    s=0
    while(n>0):
        r = n%10
        s += r*pow(2,i)
        n=n//10
        i=i+1
    print(f"The Binary value is {a} and Decimal Value is {s}")

bin_to_dec()
dec_to_bin()
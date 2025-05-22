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
    print(f"Decimal: {a} \t Binary: {s}")

dec_to_bin()
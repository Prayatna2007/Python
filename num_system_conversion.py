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

def oct_to_bin():
    n=input("Enter any octal number:")
    octal_digits = {'0': '000', '1': '001', '2': '010',
                    '3': '011', '4': '100', '5': '101',
                    '6': '110', '7': '111'}
    bin = ''
    for digit in n:
        bin += octal_digits[digit]
    print(f"Octal Number: {n} \t Binary Equivalent: {bin}")

print("\n\n________________________________________________________________________________________\n")
print("\t______________NUMBER SYSTEM CONVERSION_____________________\n")
while(1):
    x=(int(input("\n 1. For Decimal to Binary Converter \n 2. For Binary to Decimal Converter \n 3. For Octal to Binary \n 4. For exit \n Enter a number(1-4):- ")))
    match(x):
        case 1: dec_to_bin()
        case 2: bin_to_dec()
        case 3: oct_to_bin()
        case 4: exit(1)
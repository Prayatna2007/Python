def dec_to_bin():
    n=int(input("\n\tEnter a decimal integer:"))
    a=n
    i=0
    s=0
    while n>0:
        r = n%2
        s += r*pow(10,i)
        n=n//2
        i=i+1
    print(f"\tThe Decimal value is {a} and Binary value is {s}")

def bin_to_dec():
    n=int(input("\n\tEnter any binary number:"))
    a=n
    i=0
    s=0
    while(n>0):
        r = n%10
        s += r*pow(2,i)
        n=n//10
        i=i+1
    print(f"\tThe Binary value is {a} and Decimal Value is {s}")

def oct_to_bin():
    n=input("\n\tEnter any octal number:")
    octal_digits = {'0': '000', '1': '001', '2': '010',
                    '3': '011', '4': '100', '5': '101',
                    '6': '110', '7': '111'}
    bin = ''
    for digit in n:
        bin += octal_digits[digit]
    print(f"\tOctal Number: {n} \t Binary Equivalent: {bin}")

def hex_to_bin():
    n=input("\n\tEnter any Hexadecimal Number:")
    hex_digits = {'0': '0000', '1': '0001', '2': '0010',
                    '3': '0011', '4': '0100', '5': '0101',
                    '6': '0110', '7': '0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    bin=''
    for digit in n:
        bin+=hex_digits[digit]
    print(f"\tHexa-Decimal Number: {n} \t Binary Equivalent: {bin}")



print("\n\n\t_________________________________________________________\n")
print("\t______________NUMBER SYSTEM CONVERSION___________________\n")
while(1):
    x=(int(input("\n\n \t1. For Decimal to Binary Converter \n \t2. For Binary to Decimal Converter \n \t3. For Octal to Binary \n \t4. For Hexa Decimal to Binary \n \t5. For exit \n\t Enter a number(1-5):- ")))
    match(x):
        case 1: dec_to_bin()
        case 2: bin_to_dec()
        case 3: oct_to_bin()
        case 4: hex_to_bin()
        case 5: exit(1)
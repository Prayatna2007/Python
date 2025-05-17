def even_odd():
    try:
        a=int(input("Enter any number:"))
        if(a%2==0):
            print(f"{a} is even.")
        else:
            print(f"{a} is odd.")
    except ValueError:
        print("Please enter an integer number.....")
def pos_neg_zero():
    a=float(input("Enter any number:"))
    if(a>0):
        print(f"{a} is positive number.")
    elif(a==0):
        print(f"{a} is zero.")
    else:
        print(f"{a} is negative number.")
def prime():
    try:
        a=int(input("Enter a number: "))
        for i in range(2,a-1):
            if(a%i==0):
                break
        if(a==i):
            print(f"{a} is a prime number.")
        else:
            print(f"{a} is not a prime number.")   
    except ValueError:
            print("Please enter an integer value....\n")
while(1):
    print('''\n\n______________________Simple Program Using Match Case______________________\n''')
    print("\n\t1. For even or odd\n\t2.For Positive,Negative or Zero\n\t3.For prime or Composite\n\t4.For exit")
    x=int(input("\tEnter number from 1-4: "))
    match(x):
        case 1:    
            even_odd()
        case 2: 
            pos_neg_zero()
        case 3: 
            prime()
        case 4: 
            exit(1)

def palindrome():
    is_palindrome=True
    x=input("Enter any string:").strip()

    for i in range(0,len(x)//2):
        if(x[i]!=x[len(x)-i-1]):
            is_palindrome=False
        
    if(is_palindrome):
        print("Palindrome....")
    else:
        print("Not a palindrome...")

def rev():
    x = input("Enter any word: ").strip()
    reversed_word=""
    for i in range(len(x)-1, -1, -1):
        reversed_word += x[i]
    print(reversed_word)

while(1):
    print("Enter :\n 1. For Checking Palindrome\n 2. For Reversing String\n 3. For Exit\n\n")
    x=int(input("Enter acc to your choice (1-2) :"))
    match(x):
        case 1: 
            palindrome()
        case 2:
            rev()
        case 3:
            exit(1)


    


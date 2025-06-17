# Sorting of Numbers using List

def asc():
    list=[]
    n=int(input("Enter total terms:"))
    for i in range(n):
        a=int(input(f"Enter {i+1}: "))
        list.append(a)
    for i in range(len(list)-1):
        for j in range(i+1,(len(list))):
            if list[i]>list[j]:
                list[i]=list[i]^list[j]
                list[j]=list[i]^list[j]
                list[i]=list[i]^list[j]
    print(list)
def des():
    list=[]
    n=int(input("Enter total terms:"))
    for i in range(n):
        a=int(input(f"Enter {i+1}: "))
        list.append(a)
    for i in range(len(list)-1):
        for j in range(i+1,(len(list))):
            if list[i]<list[j]:
                list[i]=list[i]^list[j]
                list[j]=list[i]^list[j]
                list[i]=list[i]^list[j]
    print(list)

print(" 1. For Ascending Sorting \n 2. For Descending Sorting \n 3. For exit\n")
x=int(input("Enter (1-3): "))
match(x):
    case 1: asc()
    case 2: des()
    case 3: 
        exit(1)
    case _:
        print("Invalid Input...")
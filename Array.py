# A simple program where Array is used for sorting the numbers in Ascending and Descending order

from array import *

val = array('i', [])
def asc(val:list)->list:
    """
    This func takes 'n' number of input and sort them in ascending order
    """
    n = int(input("\n\t\tEnter the value for n: "))

    a = 0
    while (a < n):
        r = int(input("\t\tGive: "))
        val.append(r)
        a = a + 1

    for a in range(len(val) - 1): 
        for b in range(len(val) - 1 - a):
            if (val[b] > val[b + 1]):
                temp = val[b]
                val[b] = val[b + 1]
                val[b + 1] = temp

    print("\t\tSorted array in ascending order:")
    for x in range(len(val)):
        print("\t\t",val[x])

def des(val:list)->list:
    """
    This func takes 'n' number of input and sort them in descending order
    """
    n = int(input("\n\t\tEnter the value for n: "))

    a = 0
    while (a < n):
        r = int(input("\t\tGive: "))
        val.append(r)
        a = a + 1


    for a in range(len(val) - 1):
        for b in range(len(val) - 1 - a):
            if (val[b] < val[b + 1]):
                temp = val[b+1]
                val[b+1] = val[b]
                val[b ] = temp

    print("\t\tSorted array in Descending order:")
    for x in range(len(val)):
        print("\t\t",val[x])

print("\n\n\n\t\t1. For Ascending order\n\t\t2. For Descending Order\n\t\t3. For Exit\n")
while(2):
    x=int(input("\t\tEnter your choice(1-3): "))
    match(x):
        case 1: 
            asc(val)
        case 2:
            des(val)
        case 3:
            print("\t\tTerminating the program....................\n\t\tSuccessfully Terminated..............")
            exit(2)
        case _:
            print("Invalid Input......")
            


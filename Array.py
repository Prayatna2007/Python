from array import *

val = array('i', [])
n = int(input("Enter the value for n: "))

a = 0
while (a < n):
    r = int(input("Give: "))
    val.append(r)
    a = a + 1

# Corrected Bubble Sort algorithm
for a in range(len(val) - 1): # Outer loop for passes
    for b in range(len(val) - 1 - a): # Inner loop for comparisons and swaps
        if (val[b] > val[b + 1]):
            # Swap elements
            temp = val[b]
            val[b] = val[b + 1]
            val[b + 1] = temp

print("Sorted array in ascending order:")
for x in range(len(val)):
    print(val[x])

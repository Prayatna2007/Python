from array import *
val= array('i', [])
n=int(input("Enter the value for n: "))
a=0
while(a<n):
    r=int(input("Give: "))
    val.append(r)
    a=a+1

temp=[]
for a in range(0,len(val)-1):
    for b in range(1,len(val)):
        if(val[a]>val[b]):
            temp=val[a]
            val[a]=val[b]
            val[b]=temp

for a in range(len(val)):
    print(val[a])


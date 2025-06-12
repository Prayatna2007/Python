import numpy as np
credit_hours=[]
total_grades=[]
print("\nSIMPLE PROGRAM TO CALCULATE CGPA\n")
print("The grades in this program are : 'A+':4.0,'A':3.7,'B+':3.3,'B':3.0,'C+':2.7,'C':2.3,'F':0\n")
grades={'A+':4.0,'A':3.7,'B+':3.3,'B':3.0,'C+':2.7,'C':2.3,'F':0}
n=int(input("Enter the total no of courses:"))
print("\n")
for i in range(n):
    ch=float(input(f"Enter credit hour of {i+1} Subject:"))
    grd=(input(f"Enter the grades (i.e A+,A,...) for {i+1} Subject: "))
    credit_hours.append(ch)
    total_grades.append(grades.get(grd.upper(),0)) # set default to 0 for invalid grades
    print("\n")
ch_arr=np.array(credit_hours)
tg_arr=np.array(total_grades)
total_ch=np.sum(ch_arr)
total_gp=np.sum(ch_arr * tg_arr)
sgpa=total_gp / total_ch
print(f"Your CGPA is :- {sgpa:.2f}")

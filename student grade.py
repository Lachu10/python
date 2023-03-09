a=str(input("enter the name of the student"))
N=int(input("enter then total number of subjects"))
M=float(input("enter marks in maths"))
p=float(input("enter marks in physics"))
b=float(input("enter marks in biology"))
c=float(input("enter marks in computer science"))
t=M+p+b+c
a=t/4
print("total marks =",t)
print("aggerate of marks",a)
if(a>75):
    print(a,":distinction with all pass")
elif(a>=60 and a<75):
    print(a,":first class with distinction")
elif(a>=50 and a<60):
    print(a,":second class with distiction")
elif(a>=40 and a<50):
    print(a,":third class with distinction")
else:
    print(a,":reappear")

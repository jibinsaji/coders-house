n=int(input("enter the number"))
i=2
n1=0
n2=1
if n==1:
    print(n1)
elif n==2:
    print(n1,n2)
else:
    print(n1,n2,end="")
    while i<n:
        n3=n1+n2
        print("",n3,end="")
        n1=n2
        n2=n3
        i=i+1

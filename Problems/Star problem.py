n=int(input("Enter the Number:"))
for i in range(1,n+1):
    print(" "*  (n-i),end=" ")
    print("*" * (2*i-1),end=" ")
    print()


n=int(input("Enter the Numaber:"))
for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*(n))
    else:
        print('*',end="")
        print(" ",end="")
        print("*",end="")
        print()

#Factorial....
n=int(input("Enter the number:"))
product=1
for i in range(1,n+1):
    product=product*i
print(f'factorial of {n} is {product}')


#factorial using function and recursion
def factorial(n):
    if n==1 or n==0:
        return 1
    return n *factorial (n-1)

n=int(input('Enter the Number:'))
print(factorial(n))
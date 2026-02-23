n = int(input("Enter the Number: "))

i = 1
product = 1   # ✅ initialization

while i <= n:
    product = product * i   # ✅ multiply by i
    i += 1

print(product)

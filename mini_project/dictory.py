import random
computer = random.choice([1,2,3])
n=input("enter the choices:")
youdic={"s":1,"p":2,"g":3}
reversed_dic={1:"Snake",2:"water",3:"gun"}

you=youdic[n]

print(f"you choose:{reversed_dic[you]}\n computer choose:{reversed_dic[computer]}")
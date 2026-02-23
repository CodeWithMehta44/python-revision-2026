import random
computer = random.choice([1,2,3])
n=input("enter the choices:")
youdic={"s":1,"p":2,"g":3}
reversed_dic={1:"Snake",2:"water",3:"gun"}

you=youdic[n]

print(f"you choose:{reversed_dic[you]}\ncomputer choose:{reversed_dic[computer]}")

if(computer==you):
    print("it's Draw!!")

else:
    if(computer==1 and you==2):
        print("")
    elif(computer==1 and you==3):
        print("")
    elif(computer==1 and you==3):
        print("")
    
    
    
    
    
    
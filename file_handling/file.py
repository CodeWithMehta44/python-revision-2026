file=open("file handling/file.txt","a")
file.write("\n change the lines")
file.close()

with open("file handling/file.txt","r")as file:
    print(file.read())


with open("file handling/file.txt",'w')as file:
    file.write("this is Ashish Mehta")

    file = open("file handling/file.txt","r")
data=file.read()
print(data)
file.close()


with open('file handling/file.txt','r')as file:
    print(file.read())

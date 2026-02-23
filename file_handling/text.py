
file=open("file handling/file.txt","w")
file.write(" I am Ashish\n learing python")
file.close()

with open("file handling/file.txt","a")as file:
    file.write("\n Student of IITM \n and i will become AI ML engineer ")

with open("file handling/file.txt","r")as file:
    print(file.read())

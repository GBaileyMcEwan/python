#!/usr/bin/python3

fileVar = open("myTestFile","r")
print(fileVar.readline())
fileVar.close()

fileVar = open("myTestFile","a")
fileVar.write("Hello!\n")
fileVar.close()

#with automatically closes a file when it's done
with open("myTestFile","a") as myFile:
    myFile.write("New Line here!\n")



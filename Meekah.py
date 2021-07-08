""" testName = input("Please tell me what your name is: ")
 print(f"Hello {testName}, it is VERY nice to meet you!")

 testAge = input("Please tell me how old you are: ")
 print(f"Your age is {100-int(testAge)} less than 100!")"""

myList = input("Give me a list please (comma separated)!")
print(type(myList))


def calculateStuff(param1):
    print(f"5 x {param1} = {int(param1)*5}")


newActualList = list(myList.split(", "))
testOtherWayOfCreatingList = myList.split(", ")
newActualList.append("15")
print(type(newActualList))
print(type(testOtherWayOfCreatingList))
print(len(newActualList))
# for elementInList in myList.split(", "):
for elementInList in newActualList:
    calculateStuff(elementInList)

Strin
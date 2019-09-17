#!/usr/bin/python3

myInt=0;
myInt2=2;
while myInt < 4:
    if myInt == 0:
        myInt+=1;
        continue;
    print(str(myInt)+" is less than 4");
    myInt+=1;
print(f"{myInt} is equal to 4 not {myInt2}"); 

myInt=0;
while myInt < 4:
    if myInt == 1:
        myInt+=1;
        break;
    myInt+=1;

print(f"{myInt}");

list_of_points = [(1,2),(3,4),(5,6)];

for x,y in list_of_points:
    print(f"X is: {x} and Y is: {y}");



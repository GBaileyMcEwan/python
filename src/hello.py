#!/usr/bin/python3

print("Hello World!\n\n\n");

#print a multi-line string
print(
'''
My 
Multi
Line
String
'''
);
#concatinate 2 words
print("Pass"+"word");

#print 'Ha' 4 times
print("Ha" * 4);

#get the index of the letter 'd' in the word 'double'
print("double".find('d'));

#print a lower-case version of the string
print("This Sucks".lower());

#print special characters- double escape if you want to print a backslash
print("This rocks\tThis rocks\\t");

#If you want to use double quotes here, you would need to escape them
print("Single 'quotes' are fine but \"doubles\" are a problem");

#You can use / * + - as well as // (returns whole numbers only and ** which returns exponents and % which mods
print(2/2);

#variables are like the below
my_string = "My sample string";
my_string += " string2";
my_int = 2+2;
print(my_string + " testing ");
print(my_int);

#this is how you print a list/array
my_list = [1,2,"three",True];
print(my_list[1]);
#print the length of the list
print(len(my_list));

#s is how you print from the index position and how many items in the list you want to printt
print(my_list[3:len(my_list)]);

#You can add items to the list as per below
my_list.append(5);
print(my_list[0:]);

#you can also remove items from the list:
my_list.remove("three");
print(my_list);


print("My string is " + str(my_int) + " what");


#hashes or dictionaries are set like this
ages = {'kevin': 59, 'alex': 60}
print(ages);
print(ages['kevin']);
ages['kayla']=21;
print(ages);
ages['kayla']=22;
print(ages);
del ages['kayla'];
print(ages);
#use this as a safer way to delete an element from a hash
ages.pop('alex');
print(ages);
#print only the keys or values in the hash
print(ages.keys());
print(ages.values());
print(list(ages.values()));
#you can also create a hash/dictionary like this
weights = dict(kevin=100, bob=200);
print(weights);

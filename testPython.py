print(2*2.99)

testVariableName = "mytestVar"
num1 = 50
num2 = 5*num1
helpme = "I love cheese"

print("hello"+" "+"there"+str(5))
print(f"hello there {5*0.1} {testVariableName} {num2*num1}")


def test_function(parameter1, parameter2):
    print(f"This rocks my boeta {helpme} {parameter1*parameter2*5}")
    return(f"I am returning the following: {parameter1}")


test_function(5, 5)

# note that input functions are ALWAYS treated as strings!  If you do a calculation on them you will need to convert to a int/float
testUserInput = input("Enter something here: ")
print(f"TestUserInput was: {testUserInput}")

return_variable = test_function(5, 5)
print(f"My return variable was: {return_variable}")

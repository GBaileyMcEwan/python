#import module2
from module2 import testFunction
import os

#result = module2.testFunction("10")
result = testFunction("10")
print(f"The result was: {result}")
print(os.name)

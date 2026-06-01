import math
num=float(input("Enter any value:"))
if num<0:
     print("Please enter positive number:")
else:
     result=math.log(num)
print(f"the logorithm of {num} is : {result}")

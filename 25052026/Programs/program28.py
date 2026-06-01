def recur_facto(num):
    if num==1:
        return num
    else:
        return num*recur_facto(num-1)
num=int(input("Enter any value:"))
if num<0:
    print("The factorial does  not exist  for negative values")
elif num==0:
    print(f"The factorial of {num} is 1")
else:
    print(f"The factorial of ", num, "is" ,recur_facto(num))

#Write a Python Program to Find the Sum of Natural Numbers.
num=int(input("Enter how many numbers are sum:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(f"The sum {num} natural numbers is: {sum}")
    

#Write a Python program to swap two variables without temp variable.
a=float(input("Enter a value:"))
b=float(input("Enter b value:"))

a=a+b
b=a-b
a=a-b
print(f"a={a}\nb={b}")

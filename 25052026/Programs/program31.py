def cube_sumof_naturalnumbers(n):
    if n<=0:
        retun0
    else:
        total=sum(i**3 for i in range(1,n+1))
        return total
n=int(input("Enter any number:"))

if n<=-0:
    print("Please enter positive numbers:")
else:
    result=cube_sumof_naturalnumbers(n)
    print(f"The cube of first {n} natural numbers sum is:{result}")

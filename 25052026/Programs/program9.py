a=float(input("Enter a value:"))
b=float(input("Enter b value:"))
c=float(input("Enter c value:"))

d=(b*b)-(4*a*c)
if d>0:
    x1=(-b+d**0.5) / (2*a)
    x2=(-b+d**0.5) / (2*a)
    print(f"two real roots are {x1} and {x2}")
elif d==0:
    x=-b/(2*a)
    print(f" Equal root is {x}")
else:
    real=-b/(2*a)
    imag=((-d)**0.5) / (2*a)
    print("Complex  roots are:")
    print(real, "+", imag, "i")
    print(real, "-", imag, "i")
    

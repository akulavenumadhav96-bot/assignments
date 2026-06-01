def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Select Operation:")
print("1.Add")
print("2.Substraction")
print("3.Multiplication")
print("Division")

while True:
    choice=input("selet which operation do you perform 1,2,3,4:")
    if choice in('1','2','3','4'):
        try:
            num1=float(input("Enter num1 value:"))
            num2=float(input("Enter num2 value:"))
        except VlueError:
            print("Invalied input. Please enter a number:")
            continue
        if choice=='1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif choice=='2':
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        elif choice=='3':
            print(f"{num1} * {num2} = {mul(num1,num2)}")
        elif choice=='4':
            print(f"{num1} / {num2} = {div(num1,num2)}")

    next_calculation=input("Do want next calculation?({Yes/no)}:")
    if next_calculation=='yes':
        continue
    else:
        print("Thank You")
        break
        
            

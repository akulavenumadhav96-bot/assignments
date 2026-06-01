#Write a Python program to display calendar.
month=input("Enter month name:")
days=int(input("Enter number of days:"))
start=int(input("Enter starting day (0=Sun,1=Mon,..6=Sat):"))

print("\n",month)
print("Sun Mon Tue Wed Thu Fri Sat")
#space before first day
for i in range(start):
    print("  ",end="")
#print days
for day in range(1,days+1):
    print(f"{day:3}",end=" ")
    if (day + start)%7==0:
        print()

weight=float(input("enter your wight in kg:"))
height=float(input("enter your height in meter:"))
#print(type(height))
bmi=int(weight)/float(height)**2
print(f"Your bmi is: {bmi:.2f}")
if bmi<=18.5:
    print("Your are under weight.")
elif 18.5<bmi<24.9:
    print("Your weight is normal.")
elif 25<bmi<29.29:
    print("Your are over weight.")
else:
    print("Your are obese.")


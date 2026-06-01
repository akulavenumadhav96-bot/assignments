units=int(input("Enter units consumed:"))
if units>300:
    rate_u=6
    total_bill=(units*rate_u)/100
elif units>201 and units>300:
    rate_u=4
    total_bill=(units*rate_u)/100
elif units<101 and units>200:
    rate_u=3
    total_bill=(units*rate_u)/100
elif units<0 and units>100:
    rate_u=2
    total_bill=(units*rate_u)/100
print(total_bill)
    

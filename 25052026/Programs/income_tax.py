anual_salary=float(input("Enter person anual salary:"))
if anual_salary>1500000:
    per=30
    tax_rate=(anual_salary*per)/100
    total_net=anual_salary-tax_rate
elif anual_salary>1000000:
    per=20
    tax_rate=(anual_salary*per)/100
    total_net=anual_salary-tax_rate
elif anual_salary>500000:
    per=10
    tax_rate=(anual_salary*per)/100
    total_net=anual_salary-tax_rate
elif anual_salary<=500000:
    per=20
    tax_rate=(anual_salary*per)/100
    total_net=tax_rate-anual_salary
print("---Tax Salary---")
print(f"Anual salary : {anual_salary}")
print(f"Tax Rate : {per},({tax_rate})")
print(f"Net salary : {total_net}")

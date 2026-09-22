basic_pay = float(input("Enter the basic pay: "))

HRA = 10 / 100 * basic_pay
TA = 5 / 100 * basic_pay

salary = basic_pay + HRA + TA

print("Basic Pay =", basic_pay)
print("HRA =", HRA)
print("TA =", TA)
print("Total Salary =", salary)

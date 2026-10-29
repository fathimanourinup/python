def simple_interest(p, t, senior):
    rate = 12 if senior else 10
    return p * rate * t / 100

p = float(input("Principal: "))
t = float(input("Time (years): "))
s = input("Senior citizen? (yes/no): ")
print("Simple Interest =", simple_interest(p, t, s == "yes"))



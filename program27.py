n = int(input("Enter number of items: "))
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
total = 0
for i in numbers:
    total = total + i
print("Sum =", total)

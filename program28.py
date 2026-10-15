start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
result = []
for n in range(start, end + 1):
    if 1000 <= n <= 9999:
        digits = str(n)
        if all(int(d) % 2 == 0 for d in digits):
            root = int(n ** 0.5)
            if root * root == n:
                result.append(n)
print("Result =", result)

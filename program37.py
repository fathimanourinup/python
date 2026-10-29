def compare(s1, s2, n):
    return s1[:n] == s2[:n]

a = input("String 1: ")
b = input("String 2: ")
n = int(input("n: "))
print(compare(a, b, n))



#a
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
positive = [n for n in numbers if n > 0]
print("Positive numbers:", positive)

#b
n = int(input("Enter N: "))
squares = [i * i for i in range(1, n + 1)]
print("Squares:", squares)

#c
word = input("Enter a word: ")
vowels = [ch for ch in word if ch in 'aeiouAEIOU']
print("Vowels:", vowels)

#d
ordinal_values = [ord(ch) for ch in word]
print("Ordinal values:", ordinal_values)

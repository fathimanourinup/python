def add(*nums):
    """Returns the sum of any number of integers."""
    return sum(nums)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum =", add(*nums))
print(add.__doc__)

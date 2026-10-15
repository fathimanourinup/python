numbers=list(map(int,input("enter integers separated by spaces:").split()))
odd_numbers=[]
for num in numbers:
   if num%2!=0:
     odd_numbers.append(num)
     print("list after removing even numbers:",odd_numbers)

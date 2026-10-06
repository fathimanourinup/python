names=input("enter names:").split()
count=0
for name in names:
   count=count+name.lower().count('a')
print("number of occurances of 'a':",count)

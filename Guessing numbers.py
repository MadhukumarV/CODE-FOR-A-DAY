import random

x = random.randint(1,10)

num = int(input("Enter the number :"))
count = 1
while num != x:
  if num < x:
   print("Wrong guess enter higher")
   num = int(input("Enter the number :"))
  else:
   print("Wrong guess  enter lower")
   num = int(input("Enter the number :"))
  count += 1
else:
  print("--Jackpot Correct guess --")
  print("--You took",count,"attempts--")

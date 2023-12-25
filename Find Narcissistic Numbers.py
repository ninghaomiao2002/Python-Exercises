# Find Narcissistic Numbers
m = int(input("What number you want to start?"))
n = int(input("What number you want to end?"))
for i in range(m,n):
   a = i % 10
   b = (i % 100) // 10
   c = i // 100
   if i == a*a*a + b*b*b + c*c*c:
       print(f'{i} is the Narcissistic number between {m} and {n}.')
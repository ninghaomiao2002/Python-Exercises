# Prime Number

def prime(n):
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
    return flag

a = int(input('Enter the number you want to start from: '))
b = int(input('Enter the number you want to end with: '))
list = []
for i in range(a, b+1):
    if prime(i):
       list.append(i)
print(list)

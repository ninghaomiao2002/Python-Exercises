# 海伦公式求三角形面积

import math
a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

p = (a+b+c)/2

s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f'三角形面积是：{s}')
print('三角形面积是：%.2f' %s)



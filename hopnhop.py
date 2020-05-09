import math
from math import sqrt
x = 3
y = 4
a = int(input())
b = int(input())
power1 = float(pow((a-x),2))
power2 = float(pow((b-y),2))
power = float(power1+power2)
sqr = float(sqrt(power))
print(int(sqr))
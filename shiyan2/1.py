
import math 
a=input()
n = int(a)
sqrt_n = int(math.sqrt(n))
sq1 = sqrt_n ** 2
sq2 = (sqrt_n + 1) ** 2

if abs(n - sq1) <= abs(n - sq2):
    print(sq1)
else:
    print(sq2)

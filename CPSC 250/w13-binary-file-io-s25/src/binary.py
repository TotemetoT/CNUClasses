import sys
import math
import numpy

if len(sys.argv) < 2:
    a = int(input("Input integer value: "))
else:
    a = int(sys.argv[1])

print("System max int=", sys.maxsize)

print("a=", a)
print("b{:b}".format(a))
ab = a.to_bytes(10, byteorder='big', signed=True)
print("As bytes (big) =", ab)
al = a.to_bytes(10, byteorder='little', signed=True)
print("As bytes (little) =", al)

lg = math.floor(math.log(abs(a), 2))
sgn = 1
if a < 0:
    sgn = -1
print("sign of a=", sgn)

sum_value = 0
for i in range(lg, -1, -1):
    if 1 << i & a:  # 2**i
        sum_value += sgn * 1 << i  # 2**i
        print("  1 x 2^{:2d} = {:4d}  sum={:4d}".format(i, 2 ** i, sum_value))
    else:
        print("  0 x 2^{:2d} = {:4d}".format(i, 2 ** i))

import numpy as np
a=2.349
b=0.911

print(np.degrees(a))
print(np.degrees(b))

c=137.7
d=62.3

print(np.radians(c))
print(np.radians(d))

A=np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
    print(np.radians(i))

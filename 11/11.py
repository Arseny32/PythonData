from itertools import *
gl='OY'
col=0
for p in product('POLYGN',repeat=5):
    x=''.join(p)
    if x==x[::-1] and x[2] in gl:
        col+=1
print(col)

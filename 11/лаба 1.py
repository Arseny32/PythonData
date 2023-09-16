s=[2,3,4,7,5,12,11,13,15,16,14,14]
s=sorted(s,reverse=True)
smax=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)):
            a=s[i]
            b=s[j]
            c=s[k]
            if a+b>c and a+c>b and b+c>a:
                p=(a+b+c)/2
                ss=(p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if ss>smax:
                    smax=ss
print("Максимальная площадь треугольника", smax)



#Bai_8.20:ham e**x co hai trien taylor 
import math
x=int(input("Nhap x:"))
ex=1
n=1
t=x
while math.fabs(t)>=0.0001:
    ex +=t
    n +=1
    t *=(x/n)
print("Gia tri gan dung cua e mu x la:",ex)
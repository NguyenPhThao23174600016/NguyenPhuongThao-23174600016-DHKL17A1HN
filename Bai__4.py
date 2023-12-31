# Tinh dien tich tam giac
import math
a=int(input("Nhap canh tam giac thu nhat: "));
b=int(input("Nhap canh tam giac thu hai: "));
c=int(input("Nhap canh tam giac thu ba: "));
cv=a+b+c
p=cv/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("chu vi =", cv)
print("nua chu vi=", p)
print("dien tich=", dt)
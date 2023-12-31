#Bai 8.1:tim so lon nhat -so nho nhat
a,b,c,d=eval(input("Nhap a, b, c, d:"))
print("a, b, c, d=", a,b,c,d)
max = a
min = a
if max < b: max = b
if max < c: max = c
if max < d: max = d
if min > b: min = b
if min > c: min = c
if min > d: min = d
print("Max=", max)
print("Min=", min)

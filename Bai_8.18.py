#Bai_8.18:Kiem tra so hoan hao
x=eval(input("Nhap gia tri x:"))
S=0
for i in range(1,x):
    if (x % i == 0):
        S += i
if (S == x):
    print(x, "la so hoan hao")
else:
    print(x, "khong la so hoan hao")

#Bai_8.17:Xay dung chuong trinh nhap tu ban phim 2 so nguyen a,b.Tim BCNN(a,b)
a=int(input("Nhap so nguyen a:"))
b=int(input("Nhap so nguyen b:"))
c=a*b
for i in range (a,c+1):
    if i % a ==0 and i % b ==0:
        d=i
        break
print(i)
#bai_9.5:xay dung phuong thuc tinh A(x,n)
import math
x=int(input("Nhap gia tri x la:"))
n=int(input("Nhap gia tri n la:"))
A=(x**2+x+1)**n+(x**2-x+1)**n
print("A=" ,A)
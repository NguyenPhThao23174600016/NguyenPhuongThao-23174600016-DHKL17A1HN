#Bai_8.14:Tinh tong cua n so nguyen nhap vao
n=int(input("Nhap so nguyen n : "))
S = 0
for i in range(n):
    so_nguyen = int(input("Nhap so nguyen thu {}: ".format(i + 1)))
    S += so_nguyen
print("Tong cua cac {} so nguyen la: {}".format(n, S))
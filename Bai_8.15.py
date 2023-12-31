#Bai_8.15: Tinh tong cua cac so nguyen nhap vao, cham dut khi nhap so 0
a = True
S = 0
while a:
    print("Nhap so nguyen n: ")
    b = int(input())
    S = S + b
    if b ==0:
        a = False
        break
print("tong cac so hang vua nhap la: ",S)
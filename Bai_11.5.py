import math
A=[]
while True:
    x=int(input("nhập giá trị:"))
    A.append(x)
    tiep_tuc=input("Tiếp tục nhập giá trị? 1:Có, 0:Không : ")
    if tiep_tuc!='1':
        break

print("List:",A)
so_am = [num for num in A if num < 0 ]
so_duong = [num for num in A if num > 0 ]

#ham kiem tra so nguyen to 
def so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for num in A:
    if so_nguyen_to(num):
        print("Các số nguyên tố trong list là:",num)

print("Các phần tử âm trong list là:", so_am)
print("Các phần tử dương trong list là:",so_duong)
#trung bình cộng
tong_am = sum(so_am)
tong_duong = sum(so_duong)
pt_so_am = len(so_am)
pt_so_duong = len(so_duong)
trung_binh_am = tong_am / pt_so_am
trung_binh_duong = tong_duong / pt_so_duong
print("trung bình cộng các phần tử âm là: ", trung_binh_am )
print("trung bình cộng các phần tử dương là: ", trung_binh_duong )
max = max(A)
min = min(A)
print("Max A: ", max)
print("Min A: ", min)
tang_dan = sorted(A)
print("danh sách tăng dần là:", tang_dan)




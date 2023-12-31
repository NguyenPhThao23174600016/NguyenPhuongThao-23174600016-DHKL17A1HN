#bai_9.3:tinh chi so bmi
import math
chieu_cao=eval(input("Nhập chiều cao là:"))
can_nang=eval(input("Nhập cân nặng là:"))
bmi = can_nang/(chieu_cao*chieu_cao)
print("Chỉ số bmi của bạn là = " , bmi)
if bmi<18.5:
    print("Gầy")
elif bmi>= 18.5 and bmi <=24.99:
    print("Bình thường")
else:
    print("Thừa cân")
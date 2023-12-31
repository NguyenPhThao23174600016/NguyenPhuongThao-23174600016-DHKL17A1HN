#bai_10.8: su dung ham datetimes
import calendar
from datetime import datetime
ngay=eval(input("Nhap ngay la: "))
thang=eval(input("Nhap thang la: "))
nam=eval(input("Nhap nam la: "))
print("Ngay thang nam vua nhap la:",)
if nam%4==0 and nam%100==0:
    print("Nam",nam,"la nam nhuan")
else:
    print("Nam",nam,"khong phai la nam nhuan")
    

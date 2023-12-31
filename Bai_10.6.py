#BAI_10.6:Giai phuong trinh bac 2
import math
a,b,c=eval(input("Nhap he so a,b,c la:"))
delta=b**2-4*a*c
if delta < 0:
    print("Phuong trinh co vo nghiem")
elif delta == 0:
    print("Phuong trinh co vo so nghiem")
    print("Nghiem cua phuong trinh la: x=",-b/2*a)
else:
    print("Phuong trinh co 2 nghiem phan biet")
    print("Nghiem 1 la: x1=",(-b+math.sqrt(delta))/(2*a))
    print("Nghiem 2 la: x2=",(-b-math.sqrt(delta))/(2*a))

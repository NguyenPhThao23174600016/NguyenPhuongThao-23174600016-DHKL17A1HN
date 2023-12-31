#Bai_8.5:Kiem tra nam nhuan
a = eval(input("Nhap year: "))
if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print("nam", a, "la nam nhuan")
else:
    print("nam", a, "khong phai nam nhuan")

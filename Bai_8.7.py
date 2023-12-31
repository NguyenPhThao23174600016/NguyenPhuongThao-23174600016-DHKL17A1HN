#Bai_8.7:Tinh tien dien
a=eval(input("Nhap so kwh tieu thu:"))
if a>=0:
    if a<=50:
       print("tong so tien phai tra:",a*1678,"dong.")
    elif a<=100:
       print("tong so tien phai tra:",50*1678+(a-50)*1734,"dong.")
    elif a<=200:
       print("tong so tien phai tra:",50*(1678+1734)+(a-100)*2014,"dong.")
    elif a<=300:
       print("tong so tien phai tra:",50*(1678+1734+2014)+(a-200)*2536,"dong.")
    elif a<=400:
       print("tong so tien phai tra:",50*(1678+1734+2014+2536)+(a-300)*2834,"dong.")
    else:
       print("tong so tien phai tra:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"dong.")     

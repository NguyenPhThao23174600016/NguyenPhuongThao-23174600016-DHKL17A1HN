#1
def tim_max_min(lon_nho):
    max = max(lon_nho)
    min = min(lon_nho)
    return max, min
#2
def  abss(x):
    x=abs(x)
    print("|x|=",x)
#3   
def giai_pt_bac_nhat(a,b):
    if a ==0:
        if b==0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem duy nhat la x= ", -b/a)
#4
import math
def dien_tich_tam_giac(a,b,c):
    if a+b<c and b+c<b:
         ("day khong phai la tam giac")
    else:
         ("day la mot tam giac")
    p=(a+b+c)/2
    S= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac tren la: ",S)
#5
def kt_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("nam", nam, "la nam nhuan")
    else:
        print("nam", nam, "khong phai nam nhuan")
#6
def tinh_phi_taxi(time_cho,loai_xe,so_km):
    tien_cuoc=float(0)
    tien_di_chuyen=float(0)
    if time_cho >=5:
        tien_cho=(time_cho-5)*0.8
    else:
        tien_cho=0
        if loai_xe==4:
            if so_km <=0.8:
                tien_di_chuyen=0.8*11000
            elif so_km <=20:
                tien_di_chuyen=0.8*11000+(20-so_km)*12100
            else:
                tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
                tien_cuoc=tien_cho+tien_di_chuyen
                print("Cuoc phi xe 4 cho la ",tien_cuoc)
        if loai_xe==7:
            if so_km <=0.8:
                tien_di_chuyen=tien_cho+0.8*13000
            elif so_km <=30:
                tien_di_chuyen=tien_cho+0.8*13000+(30-so_km)*14100
            else:
                tien_di_chuyen=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
                tien_cuoc=tien_cho+tien_di_chuyen
                print("Cuoc phi xe 7 cho la ",tien_cuoc)
#7
def tinh_tien_dien(so_dien):
    if so_dien < 0: 
         ("So kWh khong xac dinh")
    else:
        tong_tien = 0.0
    if so_dien >= 401:
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + (so_dien - 400)*2927
    elif so_dien >= 301: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + (so_dien - 300)*2834
    elif so_dien >= 201: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + (so_dien - 200)*2536
    elif so_dien >= 101: 
        tong_tien = 50*1.675 + 50*1734 + (so_dien - 100)*2014
    elif so_dien >= 51:
        tong_tien = 50*1.675 + (so_dien - 50)*1734
    else: 
        tong_tien = so_dien*1.675
    print("tiền điện cần thanh toán:",tong_tien)
#8
def tinh_gia_phong(a,b):
    if a>0 & a<=8:
        if a==1: c=1260000
        elif a==2: c=1550000
        elif a==3: c=1830000
        elif a==4: c=1830000
        elif a==5: c=2120000
        elif a==6: c=2120000
        elif a==7: c=2540000
        elif a==8: c=4800000
        else: 
            ("Vui long chon lai ma phong.")
    else:  ("Vui long chon lai ma phong.") 
    if b==1:
        print("Gia tien phong la:",c,"dong.")
    elif b==2:
        print("Gia tien phong la:",c*b*0.75,"dong.") 
    elif b==3:
        print("Gia tien phong la:",c*b*0.75,"dong.") 
    elif b>=4:
        print("Gia tien phong la:",c*b*0.7,"dong.")
    else:
        print("Vui long nhap lai so dem.")
#9
def dem_nguoc(n):
    print("Start!!!")
    while n >= 0:
        print(n)
        n -= 1
    else:
        print("End !!!")
#10
def tinh_S(x,n):
    S =((x**2+1)*n)
    print("s=(x**2+1)**n=", S)
#11
def tinh_A(x,n):
    A=(x**2+n+1)**n +(x**2-n+1)**n
    print("A=(x**2+x+1)**n+(x**2-x+1)**n=", A)
#12
def kiem_tra_so_nguyen_to(n):
    neu = True
    if n < 2 :
        print(n, "khong la so nguyen to")
    else:
        for i in range(2,n):
            if n % i ==0:
                neu = False
            break
    if neu:
        print(n, "la so nguyen to")
    else:
        print(n, "khong la so nguyen to")
#13
import math
def A(n):
    j = []
    a = 0
    for i in range(1,n+1):
        if i%2==1:
            j.append(i)
    for v in j:
        a = a + v
    return print("A = ",a)
def B(n):
    j = []
    a = 0
    for i in range(1,n+1):
        if i%2==0:
            j.append(i)
    for v in j:
        a = a + v
    return print("B = ",a)
def C(n):
    j = []
    a = 1
    for i in range(1,n+1):
        j.append(i)
    for v in j:
        a = a*v
    return print("C = ",a)
def D(n):
    j = []
    a = 1
    for i in range(1,n+1):
        if i%3==0:
            j.append(i)
    for v in j:
        a = a * v
    return print("D = ",a)
def E(n):
    j = []
    a = 0
    for i in range(2,n+1):
        if i>0:
            for k in range(2,int(math.sqrt(i))+1):
                if i%k ==0:
                    break
            else:
                j.append(i)
    for v in j:
        a = a + v
    print("E = ",a)    
def F(n):
    j = []
    a = 1
    for i in range(1,n):
        j.append(i**-1)
    for v in j:
        if i%2==0:
            a = a + v
        else:
            a = a - v 
    return print("F = ",a - 1)
#14
def tinh_tong(n):
    S = 0
    for i in range(n):
        so_nguyen = int(input("Nhap so nguyen thu {}: ".format(i + 1)))
        S += so_nguyen
        print("Tong cua cac {} so nguyen la: {}".format(n, S))
#15
def tinh_tong_so_nguyen():
    tong = 0
    while True:
        n = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
        print(n)
        tong += n
        if n == 0:
            break
    print(f"Tổng các số vừa nhập: {tong}")
#16
def tim_ucln(a, b):
    if a < 0 or b < 0:
         ("a, b phải lớn hơn 0")
         return
    min_value = min(a, b)
    for i in range(min_value, 0, -1):
        if a % i == 0 and b % i == 0:
            print(f"UCLN({a},{b}) = {i}")
            break
#17
def tim_bcnn(a,b):
    if a < 0 or b < 0:
     if a < 0 or b < 0:
         ("a, b phai lon hon 0")
    max = a
    if max < b:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            print(f"BCNN({a},{b}) = {max}")
            break
        max = max + 1
#18
def so_hoan_hao(x):
    S=0
    for i in range(1,x):
        if (x % i == 0):
            S += i
    if (S == x):
        print(x, "la so hoan hao")
    else:
        print(x, "khong la so hoan hao")
#19
def tao_day_so_moi(n):
    reversed_num = list(range(n, 0 , -1))
    print("", reversed_num)
    print("Day so le dao nguoc la:")
    for num in reversed_num:
        if num % 2 !=0:
            print("", num)

#20
def tinh_e_mu_x(n, x):
    if n < 0:
         ("n khong hop le")
    else:
        tong = 0
    for i in range(1,n+1):
        giai_thua = 1
        for j in range(1,i+1):
            giai_thua = giai_thua*i
        tong = tong + (x**i)/giai_thua
    print(f"e^{x} = {tong}")
  

    







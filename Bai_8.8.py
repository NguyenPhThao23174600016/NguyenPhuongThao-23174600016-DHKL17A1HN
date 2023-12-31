#Bai_8.8:Tinh tien thue phong resort
print("Cac loai ma phong:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")
a=eval(input("Nhap loai ma phong:"))
b=eval(input("Nhap so dem:"))
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
        print("Vui long chon lai ma phong.")
else: print("Vui long chon lai ma phong.") 
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

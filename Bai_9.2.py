#bai_9.2:tinh nam am lich
import math
nam=eval(input("Nhap nam la:"))
#tinh Can
if nam%10==0:
    print("Canh")
    a="Canh"
elif nam%10==1:
    print("Tân")
    a="Tân"
elif nam%10==2:
    print("Nhâm")
    a="Nhâm"
elif nam%10==3:
    print("Quý")
    a="Quý"
elif nam%10==4:
    print("Giáp")
    a="Giáp"
elif nam%10==5:
    print("Ất")
    a="Ất"
elif nam%10==1:
    print("Tân")
    a="Tân"
elif nam%10==6:
    print("Bính")
    a="Bính"
elif nam%10==7:
    print("Đinh")
    a="Đinh"
elif nam%10==8:
    print("Mậu")
    a="Mậu"
else:
    print("Kỷ")
    a="Kỷ"
#tinh Chi
if nam%12==0:  
    print("Thân")
    b="Thân"
elif nam%12==1:
    print("Dậu")
    b="Dậu"
elif nam%12==2:
    print("Tuất")
    b="Tuất"
elif nam%12==3:
    print("Hợi")
    b="Hợi"
elif nam%12==4:
    print("Tý")
    b="Tý"
elif nam%12==5:
    print("Sửu")
    b="Sửu"
elif nam%12==6:
    print("Dần")
    b="Dần"
elif nam%12==7:
    print("Mão")
    b="Mão"
elif nam%12==8:
    print("Thìn")
    b="Thìn"
elif nam%12==9:
    print("Tỵ")
    b="Tỵ"
elif nam%12==10:
    print("Ngọ")
    b="Ngọ"
else:
    print("Mùi")
    b="Mùi"
print("Nam", nam, "lich am la nam",a,b )
#bai_9.9:lambda
#hay su dung ham lambda de tinh 
#-dien tich,chu vi hinh tron 
#-dien tich,chu vi hinh chu nhat
import math
r,a,b=eval(input("Nhập bán kính,chiều dài,chiều rộng là:"))
#hinh tron
S1=3.14*(r**2)
P1=2*3.14*r
print("Diện tích hinh tron la:" ,S1)
print("Chu vi hinh tron la:" ,P1)
#hinh chu nhat
S2=a*b
P2=(a+b)*2
print("Dien tich hinh chu nhat la:" ,S2)
print("Chu vi hinh chu nhat la:" , P2)
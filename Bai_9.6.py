#bai_9.6:kiem tra so nguyen to 
n=eval(input("Nhap n: "))
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
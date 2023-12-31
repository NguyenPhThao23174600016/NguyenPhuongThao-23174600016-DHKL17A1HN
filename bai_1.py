try:
    a, b, c = map(float, input("Nhap 3 canh cua tam giac: ").split())
    if a <= 0  or b <= 0 or c <= 0:
        raise ValueError
    if a <= 0 or b <= 0 or c <=0 or a + b <= c or b + c <= a or a + c <= b:
        raise ValueError
except  ValueError as e:
    print("Lỗi thử lại !!!")
else:
    print("Ba cạnh đúng là cạnh của tam giác !!!")
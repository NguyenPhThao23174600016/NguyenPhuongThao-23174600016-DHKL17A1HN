so_truoc = [None, None, None]
while True:
        try:
            x = int(input("Nhập một số nguyên dương (0:kết thúc): "))
            so = int(x)
            if so < 0:
                raise ValueError
            elif so == 0:
                break
            elif so == so_truoc[0] == so_truoc[1] == so_truoc[2]:
                raise ValueError
            else:
                so_truoc = [so, so_truoc[0], so_truoc[1]]
        except ValueError as e:
            print("lỗi ,vui lòng nhập lại")


#Bai_8.19: Dao nguoc so
n=eval(input("Nhap vao mot day so:"))
reversed_num = list(range(n, 0 , -1))
print("", reversed_num)
print("Day so le dao nguoc la:")
for num in reversed_num:
    if num % 2 !=0:
        print("", num)
# Tạo một tuple có 10 phần tử chuỗi bất kỳ
my_tuple = ('red', 'green', 'blue', 'white', 'black', 'pink', 'orange', 'yellow', 'red', 'blue')

# Nhập index dương và âm
index_duong = int(input("Nhập index dương (0<=index<10) : "))
index_am = int(input("Nhập index âm (-1>index>=-9)"))
# In tuple
print("Tuple của bạn là: ",my_tuple)

# In giá trị của phần tử trong tuple có index dương và âm đã nhập
if index_duong >= 0:
    print("Giá trị của phần tử có index dương:",[index_duong],my_tuple[index_duong])
if index_am < 0:
    print("Giá trị của phần tử có index âm:",[index_am],my_tuple[index_am])

# Nhập chuỗi cần tìm
s_find = input("Nhập chuỗi cần tìm: ")

# Tìm và đếm số lần xuất hiện của s_find trong tuple bằng Python
count = my_tuple.count(s_find)
print(f"Số lần xuất hiện của chuỗi '{s_find}' trong tuple là: {count}")

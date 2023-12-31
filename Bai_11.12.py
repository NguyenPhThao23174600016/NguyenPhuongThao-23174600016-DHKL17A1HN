#Tạo tuple a và b
a = input("Nhập 4 số nguyên dương đầu tiên là:").split(' ')
b = input("Nhập 4 số nguyên dương tiếp theo là:").split(' ')
tuple_a = a
tuple_b = b
print("Tuple a là:",tuple_a)
print("Tuple b là:",tuple_b)
# Tạo một tuple c là sự kết hợp của các phần tử trong tuple a và b
tuple_c = tuple_a + tuple_b
print("Tuple c là:",tuple_c)
# Tạo một tuple d từ tuple c với các phần tử được sắp xếp
d = tuple(sorted(tuple_c))
tuple_d = d
print("Tuple d là:",(tuple_d))
# In phần tử thứ 3 của d
print("Phần tử thứ 3 của tuple d là:", tuple_d[2])
# In 3 phần tử cuối cùng của d
print("3 phần tử cuối cùng của tuple d là:", tuple_d[-3:])

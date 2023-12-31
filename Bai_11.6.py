chieu_cao = list(map(int,input("Nhập chiều cao là:").split (',')))
chieu_cao_met = [num * 0.0254 for num in chieu_cao]
print("chiều cao theo đơn vị inch là: ", chieu_cao)
print("chiều cao theo đơn vị mét là: ", chieu_cao_met)

print("3 chiều cao đầu tiên:", chieu_cao_met[:3])
print("3 chiều cao cuối cùng:", chieu_cao_met[-3:])
A = sum(chieu_cao_met)
B = len(chieu_cao_met)
trung_binh = A / B
print("Chiều cao trung bình theo đơn vị mét là:", trung_binh)
print("Chiều cao lớn nhất:", max(chieu_cao_met))
print("Chiều cao nhỏ nhất:", min(chieu_cao_met))
chieu_cao_tang_dan = sorted(chieu_cao_met)
chieu_cao_giam_dan = sorted(chieu_cao_met, reverse=True)
print("Chiều cao tăng dần là:", chieu_cao_tang_dan)
print("Chiều cao giảm dần là:", chieu_cao_giam_dan)
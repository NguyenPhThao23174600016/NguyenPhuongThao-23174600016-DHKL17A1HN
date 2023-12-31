#Bai_7.7:doi tien voi cac menh gia:5000000,200000,100000,50000
so_tien_muon_doi=int(input("Nhap so tien muon doi :"))
so_to_1 = so_tien_muon_doi // 500000
tien_con_lai_1 = so_tien_muon_doi % 500000
print("so_to_500000 =",so_to_1)
so_to_2 = tien_con_lai_1 // 200000
tien_con_lai_2 = tien_con_lai_1 % 200000
print("so_to_200000 =",so_to_2)
so_to_3 = tien_con_lai_2 // 100000
tien_con_lai_3 = tien_con_lai_2 % 100000
print("so_to_100000 =",so_to_3)
so_to_4 = tien_con_lai_3 // 50000
tien_con_lai_4= tien_con_lai_3 % 50000
print("so_to_50000 =",so_to_4)
print("tien_con_lai =", tien_con_lai_4)

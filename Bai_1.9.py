#bai_1.9:tinh tien lai gui tiet kiem
lai_suat_mot_nam=eval(input("Nhap lai suat mot nam="))
so_tien_gui=eval(input("Nhap so tien gui="))
so_thang_gui=eval(input("Nhap so thang gui="))
tien_lai=(so_tien_gui*so_thang_gui)*(lai_suat_mot_nam/100/12)
tien_von_lai=so_tien_gui+tien_lai
print("tien lai:",tien_lai)
print("tien von+lai:",tien_von_lai)

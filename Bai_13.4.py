from xu_ly_tap_tin import *
while True:
    name = input("Nhập tên tập tin txt: ")
    new = input("Nhập nội dung : ")
    ghi_noi_dung_vao_tap_tin(name, new)
    if not tiep_tuc():
        break
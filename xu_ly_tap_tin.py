def bai_13_1():
    with open('HumptyDumpty.txt','r') as file:
        f = file.read()
        print("Nội dung tập tin: ", f)

def bai_13_2(ten):
    with open(ten,'r') as file:
            f = file.read()
            lines = f.count('\n')
            words = len(f.split())
            chars = len(f)
            print("Content of file: ", f)
            print("Lines:",lines,"Words:",words,"Chars:",chars)
      
def bai_13_3(ten):
      with open(ten,'r') as file:
            ten = file.read()
            print("Nội dung: ", ten)
def ghi(ten,noi_dung):
    with open(ten, 'a+') as file:
        file.write(noi_dung)

def ghi_noi_dung_vao_tap_tin(name, new):
    try:
        try:
            with open(name, 'r', encoding='utf-8') as file_old:
                old= file_old.read()
        except FileNotFoundError:
            old = None
        with open(name, 'a', encoding='utf-8') as file:
            if old is not None:
                file.write('\n')
            file.write(new)
        print("Đã ghi nội dung vào tập tin",file)
    except Exception as e:
        print(f"Lỗi: {e}")
def tiep_tuc():
    while True:
        chon = input("Bạn có muốn tiếp tục ghi nội dung vào file? 1:có 2:không ")
        if chon == '1':
            return True
        elif chon == '0':
            return False
        else:
            print("Chọn không hợp lệ. Vui lòng chọn lại.")

import csv
def mo_file_csv():
    try:
        with open('file.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Danh sách không tồn tại: ")

import csv
def ghi_csv_file(ten_tap_tin, noi_dung):
    with open(ten_tap_tin, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(noi_dung)

def doc_csv_file(ten_tap_tin):
    with open(ten_tap_tin, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
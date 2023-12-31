A=[]
while True:
    x=input("Nhập giá trị:")
    A.append(x)
    tiep_tuc=input("Tiếp tục nhập giá trị? 1:có, 0:không  ")
    if tiep_tuc!='1':
        break
print("List là:",A)
thresh = input("Nhập thresh:")
ket_qua = [ i > thresh for i in A ]
print("kết quả: ", ket_qua)   
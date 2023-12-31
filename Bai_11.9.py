# xác định khách có đến dự tiệc muộn hay không 
def party_late(arrivals,name):
    # trả về True nếu khách đến trễ
    # trả về False nếu khách không đến trễ
    khach = arrivals.index(name) #tìm vị trí khách trong dsach
    khach_den_truoc = khach
    khach_den_tre = khach_den_truoc > len(arrivals)/2
    return khach_den_tre
arrivals = ['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
print(party_late(arrivals,name= 'Gilbert'))
print(party_late(arrivals,name= 'Fleda'))
print(party_late(arrivals,name= 'Mona'))
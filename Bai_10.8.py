import calendar
from datetime import datetime
date = input("Nhập ngày tháng năm theo dd/mm/yyyy: ")
date_new= datetime.strptime(date,"%d/%m/%Y")
print("Theo định dạng ngày - tháng - năm: ",date_new.strftime("%d-%m-%Y"))
year = int(input("Nhập năm là: "))
if calendar.isleap(year):
    print(year, "là năm nhuận")
else:
    print(year, "không phải là năm nhuận")
weekday = date_new.weekday()
days = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
print("Ngày", date_new.strftime("%d-%m-%Y"), "là", days[weekday])
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
days_in_month = calendar.monthrange(year, month)[1]
print("Tháng", month, "năm", year, "có", days_in_month, "ngày")
   
